from dice.entity.dice import Dice
from game.entity.game import Game
from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):

    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__gameList = []

        return  cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def makeGame(self, playerId1, playerId2):
        game = Game(playerId1, playerId2)
        self.__gameList.append(game)


    # def getGameResult(self):
    #     for game in self.__gameList:
    #         if game.getGameResult() ==

