from convolution_neural_network.repository.cnn_repository_impl import ConvolutionNeuralNetworkRepositoryImpl
from convolution_neural_network.service.cnn_service import ConvolutionNeuralNetworkService


class ConvolutionNeuralNetworkServiceImpl(ConvolutionNeuralNetworkService):
    def __init__(self):
        self.convolutionNeuralNetworkRepositoryImpl = ConvolutionNeuralNetworkRepositoryImpl()

    def imageTrain(self):
        print("service -> imageTrain()")

        # 발음 주의
        (trainImages, trainLabels), (testImages, testLabels) = (
            self.convolutionNeuralNetworkRepositoryImpl.loadCifar10Data())

        print(f"trainLabels: {trainLabels}, testLabels: {testLabels}")

