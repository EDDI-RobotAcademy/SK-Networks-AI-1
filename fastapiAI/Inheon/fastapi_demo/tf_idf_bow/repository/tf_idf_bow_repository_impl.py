from abc import ABC, abstractmethod

class TfIdfBowRepository(ABC):
    @abstractmethod
    def findSimlar(self, message, countVectorizer, countMatrix):
        pass

    @abstractmethod
    def documentVectorization(self):
        pass