from game.repository.game_repository import GameRepository
from game.entity.game import Game
# from product.entity.product.Dice import getPlayerId,

class GameRepositoryImpl(GameRepository):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__diceList = []
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def getWinner(self, firstdice, firstplayer, seconddice, secondplayer):
        game = Game(firstdice, seconddice)
        g1 = game.getFirstDice()
        g2 = game.getSecondDice()

        if g1.getDiceNumber() > g2.getDiceNumber():
            return f"[{g1.getDiceNumber()} vs {g2.getDiceNumber()}] ---->  {firstplayer.getPlayerId()}-{firstplayer.getNickname()} win! "
        elif g1.getDiceNumber() < g2.getDiceNumber():
            return f"[{g1.getDiceNumber()} vs {g2.getDiceNumber()}] ----> {secondplayer.getPlayerId()}-{secondplayer.getNickname()} win!"
        else:
            return '비김'