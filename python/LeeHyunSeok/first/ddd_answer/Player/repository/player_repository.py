from abc import ABC, abstractmethod

@abstractmethod
class PlayerRepository(ABC):

    @abstractmethod
    def match(self, playerid, playernickname):
        pass

    @abstractmethod
    def getplayerid(self, playerid):
        pass

    def getplayernickname(self, playernickname):
        pass