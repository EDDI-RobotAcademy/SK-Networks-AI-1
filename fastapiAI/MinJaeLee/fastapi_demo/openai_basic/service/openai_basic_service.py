from abc import ABC, abstractmethod


class OpenAIBasicService(ABC):
    @abstractmethod
    def letsTalk(self, userSendMessage):
        pass
