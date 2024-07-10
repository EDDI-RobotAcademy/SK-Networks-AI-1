import numpy as np

from convolution_neural_network.repository.cnn_repository_impl import ConvolutionNeuralNetworkRepositoryImpl
from convolution_neural_network.service.cnn_service import ConvolutionNeuralNetworkService


class ConvolutionNeuralNetworkServiceImpl(ConvolutionNeuralNetworkService):
    # https://www.cs.toronto.edu/~kriz/cifar.html
    # 고양이(3), 강아지(5)
    TARGET_CIFAR10_CLASSES = [3, 5]
    CIFAR10_INPUT_SHAPE = (32, 32, 3)

    targetClassName = ['고양이', '개']

    def __init__(self):
        self.convolutionNeuralNetworkRepository = ConvolutionNeuralNetworkRepositoryImpl()
    def imageTrain(self):
        print("service -> controller")

        # 데이터 불러오기
        (trainImageList, trainLabelList), (testImageList, testLabelList) = (
            self.convolutionNeuralNetworkRepository.loadCifar10Data()
        )

        # print(f"trainImages: {trainImages}, trainLabels: {trainLabels}")

        # 필터링
        trainImageList, trainLabelList = self.convolutionNeuralNetworkRepository.filteringClasses(
            trainImageList, trainLabelList, self.TARGET_CIFAR10_CLASSES
        )
        testImageList, testLabelList = self.convolutionNeuralNetworkRepository.filteringClasses(
            testImageList, testLabelList, self.TARGET_CIFAR10_CLASSES
        )

        trainImageList = trainImageList.astype('float32') # 소수점 정보들도 학습 하는데 도움이 되기때문에 float
        testImageList = testImageList.astype('float32') # 정수로 하면 소수점 이하의 수를 버림

        # 데이터 보기 편하도록 증감 기법 사용
        trainGenerator, testGenerator = (
            self.convolutionNeuralNetworkRepository.createDataGenerator(
                trainImageList, trainLabelList, testImageList, testLabelList
            )
        )

        # 학습에 사용 도리 모델 생성
        numberOfClass = len(self.TARGET_CIFAR10_CLASSES)
        model = self.convolutionNeuralNetworkRepository.createModel(
            self.CIFAR10_INPUT_SHAPE, numberOfClass
        )

        compiledModel = self.convolutionNeuralNetworkRepository.modelCompile(model)
        fittedModel = self.convolutionNeuralNetworkRepository.fitModel(
            compiledModel, trainGenerator, testGenerator
        )

        fittedModel.save('cnn_model.h5')

    def imagePredict(self, file):
        image = self.convolutionNeuralNetworkRepository.readImageFile(file)
        loadedModel = self.convolutionNeuralNetworkRepository.loadModel('cnn_model.h5')
        prediction = self.convolutionNeuralNetworkRepository.predict(image, loadedModel)

        predictedClass = self.targetClassName[np.argmax(prediction)]
        return predictedClass

    def modelEvaluate(self):
        # 모델 로드
        loadedModel = self.convolutionNeuralNetworkRepository.loadModel('cnn_model.h5')

        (_, _), (testImageList, testLabelList) = (
            self.convolutionNeuralNetworkRepository.loadCifar10Data())


        testImageList, testLabelList = (
            self.convolutionNeuralNetworkRepository.filteringClasses(
            testImageList, testLabelList, self.TARGET_CIFAR10_CLASSES))

        testImageList = testImageList.astype('float32') / 255.0

        predictionList = loadedModel.predict(testImageList)
        predictedClassList = np.argmax(predictionList, axis=1)

        # print(f"predictionList: {predictionList}, predictedClassList: {predictedClassList}")

        accuracy = self.convolutionNeuralNetworkRepository.checkAccuracy(testLabelList, predictedClassList)
        precision = self.convolutionNeuralNetworkRepository.checkPrecision(testLabelList, predictedClassList)
        recall = self.convolutionNeuralNetworkRepository.checkRecall(testLabelList, predictedClassList)
        f1score = self.convolutionNeuralNetworkRepository.checkF1Score(testLabelList, predictedClassList)

        evaluatePerformance = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1Score": f1score
        }

        return evaluatePerformance