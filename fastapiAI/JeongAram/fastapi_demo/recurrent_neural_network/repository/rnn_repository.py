from abc import ABC, abstractmethod

class RecurrentNeuralNetworkRepository(ABC):
    @abstractmethod
    def build(self, rnnModel, batchSize):
        pass

    @abstractmethod
    def compile(self, RnnModel):
        pass

    @abstractmethod
    def createRnnModel(self, vocabSize, embaddingDimension, rnnUnits, batchSize):
        pass
    @abstractmethod
    def printModelSummary(self, buildRnnModel):
        pass

    @abstractmethod
    def createData(self, vocabSize, numberOfSample, sequenceLength):
        pass

    @abstractmethod
    def train(self, x, y, compiledRnnModel, batchSize):
        pass

    @abstractmethod
    def loadModel(self):
        pass

    @abstractmethod
    def generateText(self, loadedRnnModel, inputText):
        pass


