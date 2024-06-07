class Dice:
    # '__' 언더바 두 개는 접근 제한자의 역할로 private를 의미한다.
    # 그러므로 외부에서 '__'가 있는 정보를 함부로 수정 할 수 없다.
    def __init__(self):
        self.__diceNumber = 0
        self.__playerId = None

    def setDiceNumber(self, number):
        self.__diceNumber = number

    def getDiceNumber(self):
        return self.__diceNumber

    def setPlayerId(self, playerId):
        self.__playerId = playerId

    def getPlayerId(self):
        return self.__playerId


dice = Dice()
dice.__diceNumber = 3
print(dice.__diceNumber)