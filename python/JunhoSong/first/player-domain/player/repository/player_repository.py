from abc import ABC, abstractmethod

class PlayerRepository(ABC):
    @abstractmethod
    def getNickname(self, playerId):
        pass

    def checkPlayer(self, playerId):
        pass