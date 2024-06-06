from abc import ABC, abstractmethod


class PlayerService(ABC):
    @abstractmethod
    def registerPlayer(self, nickname):
        pass

    @abstractmethod
    def findPlayerByNickname(self, nickname):
        pass

    @abstractmethod
    def getPlayerList(self):
        pass