import numpy as np

from convolution_neural_network.repository.cnn_repository_impl import ConvolutionNeuralNetworkRepositoryImpl
from convolution_neural_network.service.cnn_service import ConvolutionNeuralNetworkService


class ConvolutionNeuralNetworkServiceImpl(ConvolutionNeuralNetworkService):
    # https://www.cs.toronto.edu/~kriz/cifar.html
    # 비행기(0), 자동차(1), 새(2), 사슴(4), 개구리(6), 말(7), 배(8), 트럭(9)
    # 고양이(3), 개(5)
    TARGET_CIFAR10_CLASSES = [3, 5]
    CIFAR10_INPUT_SHAPE = (32, 32, 3)

    targetClassName = ['고양이', '개']

    def __init__(self):
        self.convolutionNeuralNetworkRepositoryImpl = ConvolutionNeuralNetworkRepositoryImpl()

    def imageTrain(self):
        print("service -> imageTrain()")

        # 발음 주의
        (trainImageList, trainLabelList), (testImageList, testLabelList) = (
            self.convolutionNeuralNetworkRepositoryImpl.loadCifar10Data())

        trainImageList, trainLabelList = self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(
            trainImageList, trainLabelList, self.TARGET_CIFAR10_CLASSES
        )
        testImageList, testLabelList = self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(
            testImageList, testLabelList, self.TARGET_CIFAR10_CLASSES
        )

        trainImageList = trainImageList.astype('float32')
        testImageList = testImageList.astype('float32')

        trainGenerator, testGenerator = (
            self.convolutionNeuralNetworkRepositoryImpl.createDataGenerator(
                trainImageList, trainLabelList, testImageList, testLabelList
            ))

        numberOfClass = len(self.TARGET_CIFAR10_CLASSES)
        model = self.convolutionNeuralNetworkRepositoryImpl.createModel(
                                    self.CIFAR10_INPUT_SHAPE, numberOfClass)

        compiledModel = self.convolutionNeuralNetworkRepositoryImpl.modelCompile(model)
        fittedModel = self.convolutionNeuralNetworkRepositoryImpl.fitModel(
                                    compiledModel, trainGenerator, testGenerator)

        fittedModel.save('cnn_model.h5')

    def imagePredict(self, file):
        print("service -> imagePredict()")

        image = self.convolutionNeuralNetworkRepositoryImpl.readImageFile(file)
        print("service -> imagePredict(): after readImageFile()")

        loadedModel = self.convolutionNeuralNetworkRepositoryImpl.loadModel('cnn_model.h5')
        print("service -> imagePredict(): after loadModel()")

        prediction = self.convolutionNeuralNetworkRepositoryImpl.predict(image, loadedModel)
        print(f"prediction: {prediction}")

        predictedClass = self.targetClassName[np.argmax(prediction)]
        return predictedClass

    def modelEvaluate(self):
        loadedModel = self.convolutionNeuralNetworkRepositoryImpl.loadModel('cnn_model.h5')

        (_, _), (testImageList, testLabelList) = (
            self.convolutionNeuralNetworkRepositoryImpl.loadCifar10Data())

        testImageList, testLabelList = (
            self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(
                testImageList, testLabelList, self.TARGET_CIFAR10_CLASSES))

        testImageList = testImageList.astype('float32') / 255.0

        predictionList = loadedModel.predict(testImageList)
        predictedClassList = np.argmax(predictionList, axis=1)

        # print(f"predictionList: {predictionList}, predictedClassList: {predictedClassList}")

        accuracy = self.convolutionNeuralNetworkRepositoryImpl.checkAccuracy(
                                                testLabelList, predictedClassList)
        precision = self.convolutionNeuralNetworkRepositoryImpl.checkPrecision(
                                                testLabelList, predictedClassList)
        recall = self.convolutionNeuralNetworkRepositoryImpl.checkRecall(
                                                testLabelList, predictedClassList)
        f1Score = self.convolutionNeuralNetworkRepositoryImpl.checkF1Score(
                                                testLabelList, predictedClassList)

        evaluatedPerformance = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1Score": f1Score,
        }

        return evaluatedPerformance
