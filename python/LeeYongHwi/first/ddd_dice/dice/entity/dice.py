class Dice:
    # '__' 언더바 두 개는 접근 재현자의 역할로 private을 의미합니다.
    # 그러므로 외부에서 '__'가 있는 정보를 함부로 수정할 수 없습니다.
    # 협력할 때 임의로 수정할 수 없게 하기 위해
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


dice = Dice()