from dice.entity.dice import Dice
from dice.entity.DiceNumber import DiceNumber
from dice.repository.dice_repository import DiceRepository
import random


# 파이썬 상속은 아래와 같이 class A(상속할 클래스) 형태로 상속을 진행
class DiceRepositoryImpl(DiceRepository):
    # Singleton(싱글톤) 객체를 만들기 위한 기법 시작
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

    # Singleton(싱글톤) 객체를 만들기 위한 기법 끝
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
                return dice

        return None

