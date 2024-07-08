from abc import ABC, abstractmethod


class RecurrentNeuralNetworkRepository(ABC):
    @abstractmethod
    def train(self, rnnModel, batchSize):
        pass

    @abstractmethod
    def createRnnModel(self, vocabSize, embeddingDimension, rnnUnits, batchSize):
        pass
