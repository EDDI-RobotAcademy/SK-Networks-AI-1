from abc import ABC, abstractmethod

class PolynomialRegressionService(ABC):
    @abstractmethod
    def createSamplePolynomialRegression(self):
        pass