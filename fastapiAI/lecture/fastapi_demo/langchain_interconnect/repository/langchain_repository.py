from abc import ABC, abstractmethod


class LangchainRepository(ABC):
    @abstractmethod
    def loadDocumentation(self):
        pass

    @abstractmethod
    def createTextChunk(self, documentList):
        pass

    @abstractmethod
    def createFaissIndex(self, documentList):
        pass

    @abstractmethod
    def loadLLMChain(self):
        pass

    @abstractmethod
    def createRagChain(self, llm, faissIndex):
        pass

    @abstractmethod
    def runChain(self, chain, userSendMessage):
        pass