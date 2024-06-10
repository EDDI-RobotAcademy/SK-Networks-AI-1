class Dice:
    # '__' 언더봐 두 개는 접근 제한자의 역할로 private을 의미합니다.
    # 그러므로 외부에서 '__'가 있는 정보를 함부로 수정할 수 있습니다.
    # 보안이라는 포괄적인 의미보다 사고방지의 의미로 private을 의미.
    def __init__(self):
        self.__diceNumber = 0
        self.__playerId = None

    def setDiceNumber(self, number):
        self.__diceNumber = number

    def setPlayerId(self, playerId):
        self.__playerId = playerId

    def getDiceNumber(self):
        return self.__diceNumber

    def getPlayerId(self):
        return self.__playerId

# dice = Dice()
# dice.__diceNumber = 3
# print("주사위 눈금:", dice.__diceNumber)