class Dice:
    def __init__(self):
        self.__diceNumber = 0
        self.__playerId = None


    def setDiceNumber(self, number):
        self.__diceNumber = number


    def setPlayerId(self, PlayerId):
        self.__PlayerId = PlayerId

    def getDiceNumber(self):
        return self.__diceNumber


    def getPlayerId(self):
        return self.__playerId

# dice = Dice()
# dice.__diceNumber = 3
# print("주사위 숫자 : ", dice.__diceNumber)