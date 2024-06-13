import random

from dice.entity.DiceNumber import DiceNumber
from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository

# 파이썬의 상속은 class A(상속할 클래스) 형태로 상속을 진행한다.
# 인터페이스를 상속 받아서 가져온 클래스는 반드시 인터페이스 클래스에 있는 함수들을 만들어줘야한다.
class DiceRepositoryImpl(DiceRepository):
    # Singleton(싱글톤) 객체를 만들기 위한 기법 시작
    # 싱글톤이 되면 객체는 유일성을 가지게 됩니다.
    # Entity에 있는 객체들은 여러 개가 될 수 있습니다.
    # 반면 이들을 서포트하는 Repository 객체나 Service 객체가 여러 개 존재 할 필요가 없습니다.
    # 그러므로 이들은 Singleton으로 구성하여 유일성을 가지게 만듭니다.
    # 이것은 궁극적으로 메모리라는 자원을 좀 더 효율적으로 사용하기 위해 사용하는 기법입니다.
    # (관점으로 보자면 메모리 절감으로 보면 되곘습니다)
    __instance = None

    # 이 인스턴스는 DiceRepository 구현체가 존재하는지 보는 부분
    # 저게 없으면 만들어서 ...
    # 밑에 cls 는 뭘까요? 클래스와 매서드가 서로 참조하기 위한 내부인자.
    # 객체화가 되었다면 self 를 사용했지만 __new__() 과정은 객체화가 되지 않았다 그래서
    # self 를 사용할 수 없는데 cls 인자는 클래스에 접근 가능하다.
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