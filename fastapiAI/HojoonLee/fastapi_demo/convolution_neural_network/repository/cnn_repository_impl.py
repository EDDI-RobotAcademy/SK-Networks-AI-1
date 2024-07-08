import io
from PIL import Image
import numpy as np
from keras.src.preprocessing.image import ImageDataGenerator
from fastapi import HTTPException
from convolution_neural_network.repository.cnn_repository import ConvolutionNeuralNetworkRepository

from tensorflow.keras.models import load_model
from tensorflow.keras import datasets, models, layers

class ConvolutionNeuralNetworkRepositoryImpl(ConvolutionNeuralNetworkRepository):

    def loadCifar10Data(self):
        print("repository -> loadCifar10Data()")

        return datasets.cifar10.load_data()

    def filteringClasses(self, imageList, labelList, targetClassList):
        filterMask = np.isin(labelList, targetClassList).flatten() # isin : [0~9] 중 3,5만 빼고 다 거르겠다는 의미
        filteredImageList = imageList[filterMask]
        filteredLabelList = labelList[filterMask]

        # print(f"filteredImageList: {filteredImageList}, length: {len(filteredImageList)}")
        # print(f"filteredLabelList: {filteredLabelList}, length: {len(filteredLabelList)}")

        # index, value 같이 활용하고 싶을 때 enumerate 활용
        for index, classIndex in enumerate(targetClassList): # (0, 3) , (1, 5)
            # filteredLabelList 는 [3,5]로만 구성된 list임 ex) [3, 5, 3, 3, 3, 5, 5, ...] >> length : 10000
            # 여기서 class label이 3이면 0으로 받고, class label이 5면 1로 받겠다는 의미
            filteredLabelList[filteredLabelList == classIndex] = index

        # print(f"after filteredLabelList: {filteredLabelList}, length: {len(filteredLabelList)}")
        return filteredImageList, filteredLabelList

    def createDataGenerator(self, trainImageList, trainLabelList, testImageList, testLabelList):

        # data 증강 처리 (이미지들을 학습하기 좋게 조절해주는 것)
        # 실질적으로 픽셀은 0 ~ 255에 해당함
        # 그러나 그래픽 카드는 0.xxx 도 표현할 수 있음
        # 고로 256개의 픽셀만 제어하는 것이 아니라 그 사이의 소수점 까지 모두 다룰 수 있음
        # 계산 정밀도를 높이기 위해 소수점인 0~1로 변환하는 것임

        # 이미지를 랜덤하게 40도까지 회전시키면서 학습함 (비틀어져도 파악할 수 있어야하기 때문) => 일반화성능 올리기
        # 랜덤하게 가로방향 20% 이동, 높이(세로방향)에 대해서도 동일
        # 기울어 뜨려서 분석 정밀도를 더 높임(shear)
        # 이미지를 랜덤하게 20%까지 확대, 축소하여 추가로 분석 정밀도를 높임
        # 또한 뒤집기 까지 시전하여 더더욱 정밀도를 높임 (horizontol_flip)
        # 이미지 변환 후 빈 공간이 있다면 가장 가까운 픽셀로 값을 채움(fill 옵션) >> interpolate
        trainDataGenerator = ImageDataGenerator(
            rescale=1./255,
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True, # 위아래 반전은 없는게, 실제로 그런일이 발생하지 않으므로
            fill_mode='nearest'
        )

        # 테스트때는 실제 상황에서 오는 이미지라 생각하면 변환하면 안 되므로 다른 방식들은 적용 x
        testDataGenerator = ImageDataGenerator(rescale=1./255)

        # 전처리 세팅 끝, 하지만 아직 image, label type은 nparray임 -> tensor화 시켜야 함
        trainGenerator = trainDataGenerator.flow(trainImageList, trainLabelList, batch_size=32)
        testGenerator = testDataGenerator.flow(testImageList, testLabelList, batch_size=32)

        return trainGenerator, testGenerator

    def createModel(self, inputShape, numberOfClass):
        # 모델 초기 세팅
        model = models.Sequential()

        # model 구조 만들기

        # feature extractor 부분
        # 모델 구조는 거의 conv - pooling의 반복이라 보면 됨
        # Conv2D(채널개수, (커널 크기))
        # 총 32개의 필터를 사용해서 (3x3) 행렬로 전체 이미지를 스캔합니다.
        model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=inputShape)) # conv filter 적용
        # (2,2) 크기로 전체를 스캔하면서 이미지의 최대값을 출력합니다.
        # 최대값만 뽑기 때문에 세부사항이 묻혀서 사실상 다운 샘플링이 됩니다. (최대값으로 묻어버려서 정확한 표현이 안되기 때문)
        # 그리고 최대값만 뽑기 때문에 연산이나 계산시 발생하는 비용을 최소화 할 수 있습니다.
        # 결국 이를 기반으로 실질적으로 주요한 특징만 추출해 볼 수 있습니다.
        model.add(layers.MaxPooling2D(2,2)) # pooling에 의해 feature map resolution 감소
        # 점진적으로 필터(채널)을 늘리면서 계속 시도를 해봅니다.
        model.add(layers.Conv2D(64, (3,3), activation='relu'))
        model.add(layers.MaxPooling2D(2, 2))
        model.add(layers.Conv2D(128, (3,3), activation='relu'))
        model.add(layers.MaxPooling2D(2, 2))

        # classifier 부분
        # 쭉 진행하고 다차원 배열로 구성된 것을 1차원 배열(벡터)로 변환합니다.
        # Dense 레이어에서 사용할 수 있도록 만들기 위함이라 봐도 무방
        model.add(layers.Flatten()) # classifier에 분류하기 위해 flatten
        # Dense는 TensorFlow에서 신경망의 완전 연결 층(Fully Connected Layer)을 구현하는 데 사용되는 클래스입니다.
        # 최종적으로 위 모델을 통과한 이후 총 512개의 뉴런을 거치며 학습을 진행 (FC layer)
        # 계산 결과가 음수 값인 경우 0으로 만드는 작업또한 relu에서 진행됨
        model.add(layers.Dense(512, activation='relu'))
        # 최종적으로 softmax를 사용해서 이것이다 저것이다로 판정을 지원
        model.add(layers.Dense(numberOfClass, activation='softmax'))

        return model

    def modelCompile(self, model):
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model

    def fitModel(self, compiledModel, trainGenerator, testGenerator):
        compiledModel.fit(trainGenerator, epochs=1000, validation_data=testGenerator)
        return compiledModel

    def readImageFile(self, file):
        try:
            image = Image.open(io.BytesIO(file))
            return image
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"파일 읽는 중 에러 발생: {e}")

    def loadModel(self, savedModelPath):
        return load_model(savedModelPath)

    def predict(self, image, loadedModel):
        resizedImage = image.resize((32,32))
        rgbConvertedImage = resizedImage.convert('RGB')
        arrayImage = np.array(rgbConvertedImage) # numpy화 시킴 (차원 확장을 위함)
        dimExpandedArrayImage = np.expand_dims(arrayImage, axis=0) # 차원 확장, 0부분 추가 (255, 38, 4) => (0, 255, 38, 4)
        scaledImage = dimExpandedArrayImage / 255.0

        prediction = loadedModel.predict(scaledImage)

        return prediction

