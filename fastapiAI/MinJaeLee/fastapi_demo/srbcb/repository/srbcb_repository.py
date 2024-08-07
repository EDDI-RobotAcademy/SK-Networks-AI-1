from abc import abstractmethod, ABC


class SrbcbRepository(ABC):
    @abstractmethod
    def generateBotMessage(self, message):
        pass