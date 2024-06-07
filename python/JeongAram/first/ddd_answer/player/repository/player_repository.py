from abc import ABC, abstractmethod

class PlayerRepository(ABC):

    @abstractmethod
    def checkPlayer(self, playerId, nickname):
        pass

    @abstractmethod
    def getNickname(self, playerId):
        pass


