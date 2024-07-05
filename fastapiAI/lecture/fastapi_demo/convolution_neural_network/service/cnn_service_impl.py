from convolution_neural_network.repository.cnn_repository_impl import ConvolutionNeuralNetworkRepositoryImpl
from convolution_neural_network.service.cnn_service import ConvolutionNeuralNetworkService


class ConvolutionNeuralNetworkServiceImpl(ConvolutionNeuralNetworkService):
    # https://www.cs.toronto.edu/~kriz/cifar.html
    # 비행기(0), 자동차(1), 새(2), 사슴(4), 개구리(6), 말(7), 배(8), 트럭(9)
    # 고양이(3), 개(5)
    TARGET_CIFAR10_CLASSES = [3, 5]

    def __init__(self):
        self.convolutionNeuralNetworkRepositoryImpl = ConvolutionNeuralNetworkRepositoryImpl()

    def imageTrain(self):
        print("service -> imageTrain()")

        # 발음 주의
        (trainImages, trainLabels), (testImages, testLabels) = (
            self.convolutionNeuralNetworkRepositoryImpl.loadCifar10Data())

        trainImages, trainLabels = self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(
            trainImages, trainLabels, self.TARGET_CIFAR10_CLASSES
        )


