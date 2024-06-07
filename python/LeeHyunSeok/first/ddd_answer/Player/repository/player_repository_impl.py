from Player.entity.player import Player
from Player.repository.player_repository import PlayerRepository
class PlayerRepositoryImpl(PlayerRepository):

    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__playList = []

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def match(self, playerid, playernickname):
        player = Player()
        player.setplayerid(playerid)
        player.setplayernickname(playernickname)
        self.__playList.append(player)

    def getplayerid(self, playerId):
        return [player.getplayerid() for player in self.__playList if player.getPlayerId() == playerId]

    def getplayernickname(self, playerId):
        return [player.getplayernickname() for player in self.__playList if player.getPlayerId() == playerId]
