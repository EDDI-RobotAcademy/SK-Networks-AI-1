from abc import ABC, abstractmethod

class PlayerRepository(ABC):

    @abstractmethod
    def register(self, nickname):
        pass

    @abstractmethod
    def findPlayerByNickname(self, nickname):
        pass

    @abstractmethod
    def list(self):
        pass

