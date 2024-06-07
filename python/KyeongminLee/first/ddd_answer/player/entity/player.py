from dice.entity.dice import Dice

class Player:
    def __init__(self):
        self.__playerID = None
        self.__playerNickname = None

    def setPlayerNickname(self, nickname):
        self.__playerNickname = nickname

    def getPlayerNickname(self):
        return self.__playerNickname

    def setPlayerId(self, playerId):
        self.__playerId = playerId

    def getPlayerId(self):
        return self.__playerId