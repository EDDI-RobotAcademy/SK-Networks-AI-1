from abc import ABC, abstractmethod


class OrdersAnalysisRepository(ABC):

    @abstractmethod
    def prepareViewCountVsQuantity(self, dataFrame):
        pass

    @abstractmethod
    def splitTrainTestData(self, X_scaled, y):
        pass
