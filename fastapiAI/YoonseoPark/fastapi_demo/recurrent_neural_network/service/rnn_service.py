from abc import ABC, abstractmethod

class RecurrentNeuralNetworkService(ABC):
    @abstractmethod
    def textTrain(self):
        pass

    @abstractmethod
    def textPredict(self, inputText):
        pass