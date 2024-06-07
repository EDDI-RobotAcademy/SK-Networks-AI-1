from abc import ABC, abstractmethod

class PlayerRepository(ABC):

    @abstractmethod
    def registerPlayer(self, playerId, nickname):
        pass

    @abstractmethod
    def getNickname(self, playerId):
        pass

