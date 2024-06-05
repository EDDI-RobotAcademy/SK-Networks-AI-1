class Dice:
    # __ 는 접근제한자의 역할로 private를 의미합니다.
    # 그러므로 외부에서 __가 있는 정보를 함부로 수정 할 수 없습니다.
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