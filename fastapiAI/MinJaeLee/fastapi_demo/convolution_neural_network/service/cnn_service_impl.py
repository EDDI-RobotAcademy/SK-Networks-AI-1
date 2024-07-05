from convolution_neural_network.respository.cnn_repository_impl import ConvolutionNeuralNetworkRepositoryImpl
from convolution_neural_network.service.cnn_service import ConvolutionNeuralNetworkService


class ConvolutionNeuralNetworkServiceImpl(ConvolutionNeuralNetworkService):
    # cifar10 데이터 중 개(5), 고양이(3) 라벨만을 선택
    # 0:비행기, 1:자동차, 2:새, 4:사슴, 6:개구리, 7:말, 8:배, 9:트럭
    TARGET_CIFAR_CLASSES = [3, 5]

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
