from abc import ABC, abstractmethod
class PolynomialRegressionRepository(ABC):

    @abstractmethod
    def regressionAnalysis(self, X, y):
        pass