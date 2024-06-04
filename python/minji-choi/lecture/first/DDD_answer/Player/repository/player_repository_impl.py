from Player.repository.player_repository import PlayerRepository
from Player.entity.player import Player

class PlayerRepositoryImpl(PlayerRepository):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__playerList = []
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def setPlayer(self, playerId, name):
        p = Player()
        p.setPlayerId(number=playerId)
        p.setNickname(name)
        self.__playerList.append(p)
    def getNickname(self, playerId):
        return [plyer.getNickname() for plyer in self.__playerList if plyer.getPlayerId() == playerId]

    def checkPlayer(self, playerId):
        for p in self.__playerList:
            if p.getPlayerId() == playerId:
                return p

        return None

