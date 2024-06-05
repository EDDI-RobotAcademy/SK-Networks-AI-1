import random
from dice.entity.DiceNumber import DiceNumber

class Dice:
    def __init__(self):
        self.__diceNumber = random.randint(DiceNumber.ONE.value, DiceNumber.SIX.value) # 실행될 때 돌리면 되니깐

    def getDiceNumber(self):
        return self.__diceNumber
