from abc import ABC, abstractmethod

class GameRepository(ABC):

    @abstractmethod
    def makeGame(self, playerId1, playerId2):
        pass

    @abstractmethod
    def getGameResult(self):
        pass

