import random

from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__playerList = []

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getPlayerList(self, playerId, playerNickname):
        player = Player()
        player.setPlayerId(playerId)
        player.setPlayerNickname(playerNickname)
        self.__playerList.append(player)

    def getPlayer(self, playerId):
        for player in self.__playerList:
            if player.getPlayerId() == playerId:
                return player

        return None

    def checkDice(self, playerId):
        pass