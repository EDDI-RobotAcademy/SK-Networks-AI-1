from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


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

    def create(self, nickname):
        player = Player(nickname)
        self.__playerList.append(player)

    def findPlayerByNickname(self, nickname):
        for player in self.__playerList:
            if player.getPlayerNickname() == nickname:
                return player

        return None
    def list(self):
        return self.__playerList
