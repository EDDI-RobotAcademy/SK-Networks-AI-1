import random
from dice.entity.DiceNumber import DiceNumber
class Dice:
    # 게임 도메인과 합쳐지면서
    # Dice에서 사용자를 set해주는게 solid법칙에 위반됨, 굳이 얘가 처리할 필요가 없음
    def __init__(self):
        self.__diceNumber = random.randint(DiceNumber.ONE.value, DiceNumber.SIX.value)

    def getDiceNumber(self):
        return self.__diceNumber