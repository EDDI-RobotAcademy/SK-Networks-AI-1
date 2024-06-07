from abc import ABC, abstractmethod


class PlayerRepository(ABC):
    @abstractmethod
    def getPlayerList(self, playerId, playerNickname):
        pass

    @abstractmethod
    def getPlayer(self, playerId):
        pass

    @abstractmethod
    def checkDice(self, playerId):
        pass