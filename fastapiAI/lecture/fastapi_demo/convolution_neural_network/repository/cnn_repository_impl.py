from convolution_neural_network.repository.cnn_repository import ConvolutionNeuralNetworkRepository

from tensorflow.keras import datasets


class ConvolutionNeuralNetworkRepositoryImpl(ConvolutionNeuralNetworkRepository):

    def loadCifar10Data(self):
        print("repository -> loadCifar10Data()")

        return datasets.cifar10.load_data()
