from abc import ABC, abstractmethod

class PolynomialRegressionService(ABC):
    @abstractmethod
    def generateSampleData(self):
        pass

    @abstractmethod
    def createSamplePolynomialRegression(self,X, y):
        pass
