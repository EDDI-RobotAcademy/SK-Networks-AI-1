from abc import ABC, abstractmethod


class OpenAIBasicService(ABC):
    @abstractmethod
    def letsTalk(self, userSendMessage):
        pass

    @abstractmethod
    def sentimentAnalysis(self, userSendMessage):
        pass