from abc import ABC, abstractmethod


class ConvolutionNeuralNetworkRepository(ABC):
    @abstractmethod
    def loadCifar10Data(self):
        pass
