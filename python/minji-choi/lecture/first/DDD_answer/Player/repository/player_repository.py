from abc import ABC, abstractmethod

class PlayerRepository(ABC):

    @abstractmethod
    def setPlayer(self, playerId, name):
        pass

    @abstractmethod
    def getNickname(self, playerId):
        pass

    @abstractmethod
    def checkPlayer(self, playerId):
        pass