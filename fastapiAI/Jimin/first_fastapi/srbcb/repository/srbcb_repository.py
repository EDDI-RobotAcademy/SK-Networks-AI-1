from abc import ABC,abstractmethod

class SrbcbRepository(ABC):
    @abstractmethod
    def generateBotMessage(self, message):
        pass