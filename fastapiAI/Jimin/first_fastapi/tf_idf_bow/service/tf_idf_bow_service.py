from abc import ABC,abstractmethod

class TfIdfBowService(ABC):

    # 유사도가 높은 document를 찾아줘
    @abstractmethod
    def findSimilarDocumentList(self, userSendMessage):
        pass