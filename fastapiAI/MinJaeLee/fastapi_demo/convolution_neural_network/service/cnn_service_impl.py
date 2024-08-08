import numpy as np

from convolution_neural_network.respository.cnn_repository_impl import ConvolutionNeuralNetworkRepositoryImpl
from convolution_neural_network.service.cnn_service import ConvolutionNeuralNetworkService


class ConvolutionNeuralNetworkServiceImpl(ConvolutionNeuralNetworkService):
    # cifar10 데이터 중 개(5), 고양이(3) 라벨만을 선택
    # 0:비행기, 1:자동차, 2:새, 4:사슴, 6:개구리, 7:말, 8:배, 9:트럭
    TARGET_CIFAR_CLASSES = [3, 5]
    CIFAR10_INPUT_SHAPE = (32, 32, 3)

    targetClassName = ['cat', 'dog']

    def __init__(self):
        self.convolutionNeuralNetworkRepositoryImpl = ConvolutionNeuralNetworkRepositoryImpl()

    def imageTrain(self):
        print(f"service -> imageTrain()")

        # 발음 주의
        (trainImageList, trainLabelList), (
            testImageList, testLabelList) = self.convolutionNeuralNetworkRepositoryImpl.loadCifar10Data()

        print(f"trainLabels: {trainLabelList}")
        print(f"testLabels: {testLabelList}")

        trainImageList, trainLabelList = self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(trainImageList,
                                                                                                      trainLabelList,
                                                                                                      self.TARGET_CIFAR_CLASSES)

        testImageList, testLabelList = self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(testImageList,
                                                                                                    testLabelList,
                                                                                                    self.TARGET_CIFAR_CLASSES)

        trainImageList = trainImageList.astype('float32')
        testImageList = testImageList.astype('float32')

        trainGenerator, testGenerator = (
            self.convolutionNeuralNetworkRepositoryImpl.createDataGenerator(trainImageList, trainLabelList,
                                                                            testImageList, testLabelList))

        numberOfClass = len(self.TARGET_CIFAR_CLASSES)
        model = self.convolutionNeuralNetworkRepositoryImpl.createModel(self.CIFAR10_INPUT_SHAPE, numberOfClass)

        compiledModel = self.convolutionNeuralNetworkRepositoryImpl.modelCompile(model)
        fittedModel = self.convolutionNeuralNetworkRepositoryImpl.fitModel(compiledModel, trainGenerator, testGenerator)

        fittedModel.save('cnn_model.keras')

    async def imagePredict(self, file):
        print(f"service -> imagePredict()")
        image = self.convolutionNeuralNetworkRepositoryImpl.readImageFile(file)
        loadedModel = self.convolutionNeuralNetworkRepositoryImpl.loadModel('cnn_model.keras')
        prediction = self.convolutionNeuralNetworkRepositoryImpl.predict(image, loadedModel)

        predictedClass = self.targetClassName[np.argmax(prediction)]
        return predictedClass

    def modelEvaluate(self):
        loadedModel = self.convolutionNeuralNetworkRepositoryImpl.loadModel('cnn_model.keras')

        (_, _), (testImageList, testLabelList) = (self.convolutionNeuralNetworkRepositoryImpl.loadCifar10Data())

        testImageList, testLabelList = (
            self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(testImageList, testLabelList,
                                                                         self.TARGET_CIFAR_CLASSES))

        testImageList = testImageList.astype('float32') / 255.0

        predictionList = loadedModel.predict(testImageList)
        predictedClassList = np.argmax(predictionList, axis=1)

        print(f"predictionList:{predictionList}, predictedClassList:{predictedClassList}")

        accuracy = self.convolutionNeuralNetworkRepositoryImpl.checkAccuracy(testLabelList, predictedClassList)

        precision = self.convolutionNeuralNetworkRepositoryImpl.checkPrecision(testLabelList, predictedClassList)

        recall = self.convolutionNeuralNetworkRepositoryImpl.checkRecall(testLabelList, predictedClassList)

        f1Score = self.convolutionNeuralNetworkRepositoryImpl.checkF1Score(testLabelList, predictedClassList)

        evaluatedPerfomance = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1Score": f1Score,
        }
        return evaluatedPerfomance
