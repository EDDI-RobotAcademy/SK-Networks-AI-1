from player.entity.player import Player
from player.repository.player_repository import PlayerRepository
import random

class PlayerRepositoryImpl(PlayerRepository):

    # Singleton(싱글톤) 객체를 만들기 위한 기법 시작

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__playerList = []

        return  cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # Singleton(싱글톤) 객체를 만들기 위한 기법 끝

    def registerPlayer(self, playerId, nickname):
        player = Player()
        player.setPlayerId(playerId)
        player.setNickname(nickname)
        self.__playerList.append(player)

    def getNickname(self, playerId):
        return [player.getNickname() for player in self.__playerList if player.getPlayerId() == playerId]

