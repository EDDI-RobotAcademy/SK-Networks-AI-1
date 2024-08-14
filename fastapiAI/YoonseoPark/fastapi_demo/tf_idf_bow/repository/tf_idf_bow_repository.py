from abc import ABC, abstractmethod


class TfIdfBowRepository(ABC):
    @abstractmethod
    def findSimilar(self, message, countVetorizer, countMatrix):
        pass

    @abstractmethod
    def documentVectorization(self):
        pass