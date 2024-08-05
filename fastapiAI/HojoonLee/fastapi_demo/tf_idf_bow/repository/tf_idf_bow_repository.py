from abc import ABC, abstractmethod

class TfIdfBowRepository(ABC):

    @abstractmethod
    def documentVectorization(self):
        pass

    @abstractmethod
    def findSimilar(self, userSendMessage, countVectorizer, countMatrix):
        pass