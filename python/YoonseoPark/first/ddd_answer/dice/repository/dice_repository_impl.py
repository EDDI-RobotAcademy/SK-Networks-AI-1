from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository
from dice.entity.DiceNumber import DiceNumber
import random

class DiceRepositoryImpl(DiceRepository):
    # Singleton(싱글톤) 객체를 만들기 위한 기법 시작
    # 싱글톤이 되면 객체는 유일성을 가지게 됩니다.
    # Entity에 있는 객체들은 여러 개가 될 수 있습니다.
    # 반면 이들을 서포트하는 Repository 객체나 Service 객체가 여러 개 존재 할 필요가 없습니다.
    # 그러므로 이들은 Singleton으로 구성하여 유일성을 가지게 만듭니다.
    # 이것은 궁극적으로 메모리라는 자원을 좀 더 효율적으로 사용하기 위해 사용하는 기법입니다. (메모리 절감 => 비용 절감)
    # (관점으로 보자면 메모리 절감으로 보면 되겠습니다)
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__diceList = []

        return  cls.__instance

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

    def getDiceNumber(self, playerId):  # 파이썬 스타일 코드
        return [dice.getDiceNumber() for dice in self.__diceList if dice.getPlayerId() == playerId]

    def checkDice(self, playerId):  # 자바 스타일 코드
        for dice in self.__diceList:
            if dice.getPlayerId() == playerId:
                return dice

        return None
        # 파이썬 스타일 코드
        # return [dice for dice in self.__diceList if dice.getPlayerId() == playerId]
