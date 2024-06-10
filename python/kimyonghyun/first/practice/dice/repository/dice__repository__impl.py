import random

from dice.entity.dice import Dice
from dice.repository.dice_repositotry import DiceRepository
from dice.entity.DiceNumber import DiceNumber

# python에서의 상송ㄱ은 아래와 같이 클래스 안에 상속할 클래스 형태로 상속을 진행합니다.
# 인터페이스를 상속 받아서 가져온 클래스는 반드시 인터페이스 클래스에 있는 함수들을 만들어줘야 합니다.
class DiceRepositoryImpl(DiceRepository):
    # singleton(싱글톤) 객체를 만들기 위한 기법 시작
    # 싱글톤이 되면 객체는 유일성을 가지게 됩니다.
    # entity에 있는 객체들은 여러 개가 될 수 있습니다.
    # 반면 이들을 서포트하는  repository 객체나 service 객체가 여러개 존재 할 필요가 없습니다.
    # 그러므로 이들은 singleton으로 구성하여 유일성을 가지게 만듭니다.
    # 이것은 궁극적으로 메모리 라는 자원을 좀 더 효율적으로 사용하기 위해서 사용하는 기법입니다.
    # (관점으로 보자면 메모리 절감으로 보면 된다.)

    __instance =None
    # 위의 __instance는 실질적으로 DiceRepository 구현체가 존재하느냐 마느냐를 보는 부분입니다.

    # __new__를 보면 제일 이상한 부분이 cls라는 것이다.
    # 도대체 cls는 무엇인가?
    # 보편적으로 cls는 클래스와 메서드가 서로 참조하기 위해 사용하는 내부 인자입니다.
    # 인스턴스화 (즉 선언하지 않은 상태에서 class에 접근하기 위한 방법 -> cls)
    # self랑은 무슨 관계? ->
    # self는 초기화가 되야 사용이 가능하다.
    # __new__를 진행하는 과정에서 아직 객체화가 안됐음 -> 그래서 cls를 사용하여 클래스 자체에 접근했다.


    def __new__(cls):
        if cls.__instance is None: #없으면 만드는 조건문
            cls.__instance = super().__new__(cls) # 상속한 class를 생성한다.
            cls.__instance.__diceList = []
        return cls.__instance #있다면 그냥 그대로 반환
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def rollDice(self, playerID):
        diceNumber = random.randint(DiceNumber.ONE.value,DiceNumber.SIX.value)
        dice = Dice()
        dice.setDiceNumber(diceNumber)
        dice.setPlayerID(playerID)
        self.__diceList.append(dice)
    def getDiceNumber(self, playerID):
        return [dice.getDiceNumber() for dice in self.__diceList if dice.getPlayerId() == playerID]

    def checkDice(self, playerID):
        for dice in self.__diceList:
            if dice.getPlayerId() == playerID:
                return dice

        return None