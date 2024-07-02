from abc import ABC, abstractmethod

class OrdersAnalysisService(ABC):

    @abstractmethod
    def trainModel(self):
        pass

    @abstractmethod
    def predictQuantityFromModel(self, viewCount):
        pass

