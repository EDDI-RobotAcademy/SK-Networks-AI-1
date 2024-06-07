from abc import ABC, abstractmethod

class PlayerRepository(ABC):

    @abstractmethod
    def match(self, playerId, playerNickname):
        pass

    @abstractmethod
    def getPlayerId(self, playerId):
        pass
    @abstractmethod
    def getPlayerNickname(self, playerId):
        pass
