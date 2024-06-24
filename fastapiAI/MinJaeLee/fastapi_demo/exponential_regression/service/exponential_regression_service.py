from abc import ABC, abstractmethod


class ExponentialRegressionService(ABC):
    @abstractmethod
    def createSampleForExponentialRegression(self):
        pass
