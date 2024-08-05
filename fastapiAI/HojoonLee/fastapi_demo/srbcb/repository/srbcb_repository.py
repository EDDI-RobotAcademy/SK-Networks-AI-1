from abc import ABC, abstractmethod

class SrbcbRepository(ABC):
    @abstractmethod
    def generateBotMessage(self, userSendMessage):
        pass