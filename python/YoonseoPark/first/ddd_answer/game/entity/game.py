from player.entity.player import Player


class Game:

    def __init__(self, playerId1, playerId2):
        self.__gameResult = None

    def getGameResult(self):
        return self.__gameResult
