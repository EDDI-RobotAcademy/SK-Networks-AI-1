from abc import ABC, abstractmethod

class ExponentialRegressionRepository(ABC):
    @abstractmethod
    def regressionAnalysis(self):
        pass