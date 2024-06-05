class Dice:
    def __init__(self, playerId):
        self.__playerId = playerId
        self.__diceNumber = None

    def getPlayerId(self):
        return self.__playerId

    def setDiceNumber(self, diceNumber):
        self.__diceNumber = diceNumber

    def getDiceNumber(self):
        return self.__diceNumber
