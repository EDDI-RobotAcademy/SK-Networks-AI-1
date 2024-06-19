from abc import ABC, abstractmethod


class PolynomialRegressionRepository(ABC):
    @abstractmethod
    def regressionAnalysis(self):
        pass
