import numpy as np

from convolution_neural_network.repository.cnn_repository_impl import ConvolutionNeuralNetworkRepositoryImpl
from convolution_neural_network.service.cnn_service import ConvolutionNeuralNetworkService


class ConvolutionNeuralNetworkServiceImpl(ConvolutionNeuralNetworkService):
    # https://www.cs.toronto.edu/~kriz/cifar.html
    # 비행기(0), 자동차(1), 새(2), 사슴(4), 개구리(6), 말(7), 배(8), 트럭(9)
    # 고양이(3), 개(5)
    TARGET_CIFAR10_CLASSES = [3, 5]
    CIFAR10_INPUT_SHAPE = (32,32,3)
    targetClassName = ['고양이', '개']

    def __init__(self):
        self.convolutionNeuralNetworkRepositoryImpl = ConvolutionNeuralNetworkRepositoryImpl()

    def imageTrain(self):
        print("service -> imageTrain()")

        # 데이터 불러오기
        (trainImageList, trainLabelList), (testImageList, testLabelList) = (
            self.convolutionNeuralNetworkRepositoryImpl.loadCifar10Data())
        # print(f"trainImages : {trainImages}")

        # filtering
        trainImageList, trainLabelList = self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(
            trainImageList, trainLabelList, self.TARGET_CIFAR10_CLASSES
        )

        testImageList, testLabelList = self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(
            testImageList, testLabelList, self.TARGET_CIFAR10_CLASSES
        )

        # 학습을 위해 데이터 형변환 시키기
        trainImageList = trainImageList.astype('float32')
        testImageList = testImageList.astype('float32')

        # 학습, 테스트에 올릴 데이터 로더 설정 (data augmentation, loader)
        trainGenerator, testGenerator = (
            self.convolutionNeuralNetworkRepositoryImpl.createDataGenerator(
                trainImageList, trainLabelList, testImageList, testLabelList
            ))

        # 학습에 사용될 모델 생성
        numberOfClass = len(self.TARGET_CIFAR10_CLASSES)
        model = self.convolutionNeuralNetworkRepositoryImpl.createModel(self.CIFAR10_INPUT_SHAPE, numberOfClass)

        # 모델 컴파일
        compiledModel = self.convolutionNeuralNetworkRepositoryImpl.modelCompile(model)

        # fit하기 (학습)
        fittedModel = self.convolutionNeuralNetworkRepositoryImpl.fitModel(
            compiledModel, trainGenerator, testGenerator
        )
        # 학습된 모델 저장
        fittedModel.save('cnn_model.h5')

    def imagePredict(self, file):
        image = self.convolutionNeuralNetworkRepositoryImpl.readImageFile(file)
        loadedModel = self.convolutionNeuralNetworkRepositoryImpl.loadModel('cnn_model.h5')
        prediction = self.convolutionNeuralNetworkRepositoryImpl.predict(image, loadedModel)
        print(f"prediction: {prediction}")
        predictedClass = self.targetClassName[np.argmax(prediction)]

        return predictedClass

    def modelEvaluate(self):
        loadedModel = self.convolutionNeuralNetworkRepositoryImpl.loadModel('cnn_model.h5')
        # cifar10 dataset에서 test data만 가져오기
        (_, _), (testImageList, testLabelList) = self.convolutionNeuralNetworkRepositoryImpl.loadCifar10Data()

        selectedClassList = [3,5]

        # 개와 고양이 데이터만 가져오기
        testImageList, testLabelList = (
            self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(
                testImageList, testLabelList, self.TARGET_CIFAR10_CLASSES))
        # test dataset 전처리 (float화 시켜주기)
        testImageList = testImageList.astype('float32') / 255.0
        # 모델 예측
        predictionList = loadedModel.predict(testImageList)
        predictedClassList = np.argmax(predictionList, axis=1)

        # print(f"predictionList: {predictionList}, predictedClassList: {predictedClassList}")

        # 정답과 예측값 보내서 accuracy 구하기
        accuracy = self.convolutionNeuralNetworkRepositoryImpl.checkAccuracy(testLabelList, predictedClassList)
        # precision 구하기
        precision = self.convolutionNeuralNetworkRepositoryImpl.checkPrecision(testLabelList, predictedClassList)
        # recall
        recall = self.convolutionNeuralNetworkRepositoryImpl.checkRecall(testLabelList, predictedClassList)
        # f1-score
        f1_score = self.convolutionNeuralNetworkRepositoryImpl.checkF1score(testLabelList, predictedClassList)

        # 4가지 지표에 대해서 성능평가
        evaluatedPerformance = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1Score": f1_score
        }

        return evaluatedPerformance