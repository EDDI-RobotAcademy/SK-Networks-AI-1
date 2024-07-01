from abc import ABC, abstractmethod


class GradientDescentRepository(ABC):
    @abstractmethod
    def createTrainData(self):
        pass

    @abstractmethod
    def selectLinearRegressionModel(self):
        pass

    @abstractmethod
    def trainModel(self, selectedModel, X, y):
        pass
