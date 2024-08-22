from abc import ABC, abstractmethod


class TfIdfBowService(ABC):
    @abstractmethod
    def findSimilarDocumentList(self, userSendMessage):
        pass