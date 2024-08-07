from abc import ABC, abstractmethod


class TfIdfBowRepository(ABC):
    @abstractmethod
    def documentVectorization(self):
        pass

    @abstractmethod
    def findSimilar(self, message, countVectorizer, countMatrix):
        pass