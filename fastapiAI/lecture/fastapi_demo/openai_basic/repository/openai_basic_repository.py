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
    def similarityAnalysis(self, userSendMessage):
        pass

    @abstractmethod
    def openAiBasedEmbedding(self, paperTitleList):
        pass
