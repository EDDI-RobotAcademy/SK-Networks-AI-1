from abc import ABC, abstractmethod


class GradientDescentRepository(ABC):
    @abstractmethod
    def createTrainData(self):
        pass

    @abstractmethod
    def selectLinearRegressionModel(self):
        pass
    @abstractmethod
    def calcMeanSquaredError(self, y_real, y_prediction):
        pass
    @abstractmethod
    def trainModel(self, selectedModel, X, y):
        pass

    @abstractmethod
    def loadModel(self, wantToBeLoadModel):
        pass

    @abstractmethod
    def predict(self, loadedModel, tensor):
        pass