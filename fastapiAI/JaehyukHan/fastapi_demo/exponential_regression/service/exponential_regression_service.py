from abc import ABC, abstractmethod


class ExponentialRegressionService(ABC):

    @abstractmethod
    def createSampleData(self):
        pass

    @abstractmethod
    def createSampleForExponentialRegression(self):
        pass