from convolution_neural_network.repository.cnn_repository_impl import ConvolutionNeuralNetworkRepositoryImpl
from convolution_neural_network.service.cnn_service import ConvolutionNeuralNetworkService
import numpy as np

class ConvolutionNeuralNetworkServiceImpl(ConvolutionNeuralNetworkService):
    # 비행기(0), 자동차(1), 새(2), 사슴(4), 개구리(6), 말(7), 배(8), 트럭(9)
    # 고양이(3), 개(5)
    TARGET_CIFAR10_CLASSES = [3, 5]
    CIFAR_INPUT_SHAPE = (32, 32, 3)
    targetClassName = ['고양이', '개']
    def __init__(self):
        self.convolutionNeuralNetworkRepository = ConvolutionNeuralNetworkRepositoryImpl()


    def imageTrain(self):
        print('service -> imageTrain')

        (trainImageList, trainLabelList), (testImageList, testLabelList) = (
            self.convolutionNeuralNetworkRepository.loadCifar10Data())
        # print(f"trainImages: {trainImages}, trainLabels: {trainLabels}")

        trainImageList, trainLabelList = self.convolutionNeuralNetworkRepository.filteringClasses(
            trainImageList, trainLabelList, self.TARGET_CIFAR10_CLASSES)
        testImageList, testLabelList = self.convolutionNeuralNetworkRepository.filteringClasses(
            testImageList, testLabelList, self.TARGET_CIFAR10_CLASSES)

        trainImageList = trainImageList.astype('float32')
        testImageList = testImageList.astype('float32')

        trainGenerator, testGenerator = self.convolutionNeuralNetworkRepository.createDataGenerator(
            trainImageList, trainLabelList, testImageList, testLabelList)

        numberOfClass = len(self.TARGET_CIFAR10_CLASSES)
        model = self.convolutionNeuralNetworkRepository.createModel(self.CIFAR_INPUT_SHAPE, numberOfClass)

        compiledModel = self.convolutionNeuralNetworkRepository.modelCompile(model)
        fittedModel = self.convolutionNeuralNetworkRepository.fitModel(
            compiledModel, trainGenerator, testGenerator)

        fittedModel.save('cnn_model.h5')

    def imagePredict(self, file):
        image = self.convolutionNeuralNetworkRepository.readImageFile(file)
        loadedModel = self.convolutionNeuralNetworkRepository.loadModel('cnn_model.h5')
        prediction = self.convolutionNeuralNetworkRepository.predict(image, loadedModel)

        predictedClass = self.targetClassName[np.argmax(prediction)]

        return predictedClass

    def modelEvaluate(self):
        loadedModel = self.convolutionNeuralNetworkRepository.loadModel('cnn_model.h5')

        (_, _), (testImageList, testLabelList) = self.convolutionNeuralNetworkRepository.loadCifar10Data()

        selectedClassList = [3, 5]

        testImageList, testLabelList = self.convolutionNeuralNetworkRepository.filteringClasses(
            testImageList, testLabelList, self.TARGET_CIFAR10_CLASSES)

        testImageList = testImageList.astype('float32') / 255.0

        predictionList = loadedModel.predict(testImageList)
        predictedClassList = np.argmax(predictionList, axis=1)

        # print(f"predictionList: {predictionList}, predictedClassList: {predictedClassList}")

        accuracy = self.convolutionNeuralNetworkRepository.checkAccuracy(testLabelList, predictedClassList)
        precision = self.convolutionNeuralNetworkRepository.checkPrecision(testLabelList, predictedClassList)
        recall = self.convolutionNeuralNetworkRepository.checkRecall(testLabelList, predictedClassList)
        f1Score = self.convolutionNeuralNetworkRepository.checkF1Score(testLabelList, predictedClassList)

        evaluatedPerformance = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1Score": f1Score,
        }

        return evaluatedPerformance
