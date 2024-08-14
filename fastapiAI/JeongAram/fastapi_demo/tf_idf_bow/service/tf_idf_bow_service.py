from abc import ABC, abstractmethod

class TfIdfBowService(ABC):
    @abstractmethod
    def findSimilarityDocumentList(self, userSendMessage):
        pass