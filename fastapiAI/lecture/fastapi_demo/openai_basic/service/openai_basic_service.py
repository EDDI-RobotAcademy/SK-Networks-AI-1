from abc import ABC, abstractmethod


class OpenAIBasicService(ABC):
    @abstractmethod
    def letsTalk(self, userSendMessage):
        pass

    @abstractmethod
    def sentimentAnalysis(self, userSendMessage):
        pass

    @abstractmethod
    def audioAnalysis(self, audioFile):
        pass

    @abstractmethod
    def textSimilarityAnalysis(self, paperTitleList, userRequestPaperTitle):
        pass
