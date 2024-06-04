from abc import ABC, abstractmethod


class PlayerService(ABC):

    @abstractmethod
    def createPlayer(self,nickname):
        pass

    @abstractmethod
    def findPlayerBynickname(self,nickname):