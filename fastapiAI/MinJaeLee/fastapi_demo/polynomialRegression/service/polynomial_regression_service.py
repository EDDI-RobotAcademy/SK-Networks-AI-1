from abc import ABC, abstractmethod


class PolynomialRegressionService(ABC):
    @abstractmethod
    def createSampleForPolynomialRegression(self):
        pass
    @abstractmethod
    def generateSampleData(self):
        pass