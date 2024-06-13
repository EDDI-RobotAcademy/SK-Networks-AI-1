import random
from dice.entity.DiceNumber import DiceNumber

class Dice:
    def __init__(self):
        self.__diceNumber =random.randint(DiceNumber.ONE.value, DiceNumber.SIX.value)


    def getDiceNumber(self):
        return self.__diceNumber
