from player.repository.player_repository import PlayerRepository
from player.entity.player import Player

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
        p = Player(nickname)
        self.__playerList.append(p)


    def findPlayerByNickname(self, nickname):
        for p in self.__playerList:
            if p.getNickname() == nickname:
                return p

        return None

    def getList(self):
        return self.__playerList