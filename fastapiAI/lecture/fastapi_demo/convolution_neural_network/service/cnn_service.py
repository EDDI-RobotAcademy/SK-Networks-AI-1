from abc import ABC, abstractmethod


class ConvolutionNeuralNetworkService(ABC):
    @abstractmethod
    def imageTrain(self):
        pass
