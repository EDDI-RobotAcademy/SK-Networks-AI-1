from abc import ABC, abstractmethod


class ConvolutionNeuralNetworkService(ABC):
    @abstractmethod
    def imageTrain(self):
        pass

    @abstractmethod
    def modelEvaluate(self):
        pass