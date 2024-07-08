from abc import ABC,abstractmethod

class RecurrentNeuralNetworkRepository(ABC):

    @abstractmethod
    def createRnnModel(self, vocabSize, embeddingDimension, rnnUnits, batchSize):
        pass

    @abstractmethod
    def train(self, rnnModel, batchSize):
        pass