import random
from player.entity.player import Player
from player.repository.player_repository import PlayerRepository

class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__playerlist = []

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def checkPlayer(self, playerId,nickname):
        player = Player()
        player.setPlayerId(playerId)
        player.setNickname(nickname)
        self.__playerlist.append(player)

    def getNickname(self, playerId):
        return [player.getNickname() for player in self.__playerlist if player.getPlayerId() == playerId]

    def getPlayerId(self, playerId):
        for player in self.__playerlist:
            if player.getPlayerId() == playerId:
                return player

            return None


