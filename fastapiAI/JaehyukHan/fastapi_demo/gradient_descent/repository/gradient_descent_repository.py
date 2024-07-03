from abc import ABC, abstractmethod


class GradientDescentRepository(ABC):
    @abstractmethod
    def createTrainData(self):
        pass

    @abstractmethod
    def selectLinearRegressionModel(self):
        pass

    @abstractmethod
    def trainModel(self, selectedModel, X, y, learningRate=0.01, numEpoches=10000):
        pass

    @abstractmethod
    def loadModel(self, wantToBeLoadModel):
        pass

    @abstractmethod
    def predict(self, loadedModel, tensor):
        pass