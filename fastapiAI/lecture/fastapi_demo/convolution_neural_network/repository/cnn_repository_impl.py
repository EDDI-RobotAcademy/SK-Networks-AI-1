import numpy as np
from keras.src.preprocessing.image import ImageDataGenerator

from convolution_neural_network.repository.cnn_repository import ConvolutionNeuralNetworkRepository

from tensorflow.keras import datasets


class ConvolutionNeuralNetworkRepositoryImpl(ConvolutionNeuralNetworkRepository):

    def loadCifar10Data(self):
        print("repository -> loadCifar10Data()")

        return datasets.cifar10.load_data()

    def filteringClasses(self, imageList, labelList, targetClassList):
        filterMask = np.isin(labelList, targetClassList).flatten()
        filteredImageList = imageList[filterMask]
        filteredLabelList = labelList[filterMask]

        # print(f"filteredImageList: {filteredImageList}, length: {len(filteredImageList)}")
        # print(f"filteredLabelList: {filteredLabelList}, length: {len(filteredLabelList)}")

        for index, classIndex in enumerate(targetClassList):
            filteredLabelList[filteredLabelList == classIndex] = index

        # print(f"filteredLabelList: {filteredLabelList}, length: {len(filteredLabelList)}")

        return filteredImageList, filteredLabelList

    def createDataGenerator(self, trainImageList, trainLabelList, testImageList, testLabelList):
        # 실질적으로 픽셀은 0 ~ 255에 해당함
        # 그러나 그래픽 카드는 0.xxx 도 표현할 수 있음
        # (고로 256개의 픽셀만 제어하는 것이 아니라 그 사이의 소수점까지 모두 다룰 수 있음)
        # 계산 정밀도를 높이기 위해 소수점인 0 ~ 1로 변환하는 것임
        
        # 이미지를 랜덤하게 40도까지 회전시키면서 학습함 (비틀어져도 파악할 수 있어야하기 때문)
        # 랜덤하게 가로 방향 20% 이동
        # 높이(세로 방향)에 대해서도 동일
        # 기울여 뜨려서 분석 정밀도를 더 높임(shear)
        # 이미지를 랜덤하게 20%까지 확대, 축소하여 추가로 분석 정밀도를 높임
        # 또한 뒤집기까지 시전하여 더더욱 정밀도를 높임
        # 이미지 변환 이후 빈 공간이 있다면 가장 가까운 픽셀로 값을 채움(fill 옵션)
        trainDataGenerator = ImageDataGenerator(
            rescale=1./255,
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest',
        )

        testDataGenerator = ImageDataGenerator(rescale=1./255)

        trainGenerator = trainDataGenerator.flow(trainImageList, trainLabelList, batch_size=32)
        testGenerator = testDataGenerator.flow(testImageList, testLabelList, batch_size=32)

        return trainGenerator, testGenerator
