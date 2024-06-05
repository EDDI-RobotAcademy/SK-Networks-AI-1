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
        d = Dice(playerId)
        d.setDiceNumber(diceNumber)
        self.__diceList.append(d)

    # def getDiceNumber(self, playerId):
    #     return [dce.getDiceNumber() for dce in self.__diceList if dce.getPlayerId() == playerId]
    #
    def checkDice(self, playerId):
        for d in self.__diceList:
            if d.getPlayerId() == playerId:
                return d

        return None

