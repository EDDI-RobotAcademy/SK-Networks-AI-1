from abc import ABC, abstractmethod


class OpenAIBasicRepository(ABC):
    @abstractmethod
    def generateText(self, userSendMessage):
        pass

    @abstractmethod
    def sentimentAnalysis(self, userSendMessage):
        pass

    @abstractmethod
    def audioAnalysis(self, audioFile):
        pass

    @abstractmethod
    def similarityAnalysis(self, userRequestPaperTitle, faissIndex):
        pass

    @abstractmethod
    def openAiBasedEmbedding(self, paperTitleList):
        pass

    @abstractmethod
    def createL2FaissIndex(self, embeddingVectorDimension):
        pass