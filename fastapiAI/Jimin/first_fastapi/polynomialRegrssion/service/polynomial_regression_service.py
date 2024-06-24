from abc import ABC, abstractmethod


class PolynomialRegressionService(ABC):
    @abstractmethod
    def createSampleForpolynomialRegression(self):
        pass