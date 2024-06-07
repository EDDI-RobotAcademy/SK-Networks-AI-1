import random

from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository
from dice.entity.DiceNumber import DiceNumber


class DiceRepositoryImpl(DiceRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__diceList = []
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def rollDice(self, playerId):
        diceNumber = random.randint(DiceNumber.ONE.value, DiceNumber.SIX.value)
        dice = Dice()
        dice.setDiceNumber(diceNumber)
        dice.setPlayerId(playerId)
        self.__diceList.append(dice)

    def getDiceNumber(self, playerId):
        return [dice.getDiceNumber() for dice in self.__diceList if dice.getPlayerId() == playerId]

    def checkDice(self, playerId):
        for dice in self.__diceList:
            if dice.getPlayerId() == playerId:
                return dice.getDiceNumber()

        return None