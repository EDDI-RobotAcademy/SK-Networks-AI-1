from abc import ABC,abstractmethod

class RecurrentNeuralNetworkService(ABC):

    @abstractmethod
    def textTrain(self):
        pass

    @abstractmethod
    def predictText(self, inputText):
        pass