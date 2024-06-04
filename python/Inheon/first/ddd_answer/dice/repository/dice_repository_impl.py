from dice.entity.DiceNumber import DiceNumber
from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository
import random

# Alt + Insert
# Implement
# Implement List Interface

# 파이썬의 상속은 아래와 같이 class A(상속할 클래스) 형태로 상속을 진행합니다.
# 인터페이스를 상속 받아서 가져온 클래스는 반드시 인터페이스 클래스에 있는 합수들을 만들어줘야 합니다.
class DiceRepositoryImpl(DiceRepository):
    # 싱글 톤(singleton): 객체를 만들기 위한 기법. 유일하게 하나 만들어지는 객체
    # 싱글톤이 되면 객체는 유일성을 가지게 됩니다.
    # Entity에 있는 객체들은 여러 개가 될 수 있습니다.
    # 반면 이들을 서포트하는 Repository 객체나 Service 객체가 여러 개 존재 할 필요가 없습니다.
    # 그러므로 이들은 Singleton으로 구성하여 유일성을 가지게 만듭니다.
    # 이것은 궁극적으로 메모리라는 자원을 좀 더 효율적으로 사용하기 위해 사용하는 기법입니다.
    # (관점으로 보자면 메모리 절감으로 보면 되겠습니다.)

    # 막말로 여기부터

    # __instance는 실질적으로 DicdRepository 구현체가 존재하느냐 마느냐를 보는 부분입니다.
    __instance = None

    # __new__ 를 보면 제일 이상한 부분이 보이는데 cls라는 것입니다.
    # 도대체 cls가 머임??
    # 보편적으로 cls는 클래스와 매서드가 서로 참조하기 위해 사용하는 내부 인자(??ㅋㅋ 정신 나갈거 같애)
    # self랑은 무슨 관계지? 라는 생각이 보편적으로 들 수 있습니다.
    # 원래 self를 통해 접근 할 수 있었잖아
    # 근데 지금 만들고 있는 클래스는 그런 self 인자가 없단 말이지
    # 이럴 때 접근할 수 있게 해주는게 cls임

    # 원래 객체화가 되었다면 self를 사용했겠지만
    # __new__() 를 진행하는 과정에서 아직 객체화가 완료되이 않았습니다.
    # 그렇기 때문에 self를 사용할 수 없는데 이 시점에 클래스 자체에 접근할 수 있는 인자가 바로 cls입니다.
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls) # super(): parent 클래스를 생성합니다.
            cls.__instance.__dicelist = []

        return cls.__instance
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    # 여기까지 그냥 갖다 붙히면 싱글톤 완성.
    def rollDice(self, playerId):
        diceNumber = random.randint(DiceNumber.ONE.value, DiceNumber.SIX.value)
        dice = Dice()
        dice.setDiceNumber(diceNumber)
        dice.setPlayerId(playerId)
        self.__dicelist.append(dice)

    def getDiceNumber(self, playerId):
        return [dice.getDiceNumber() for dice in self.__dicelist if dice.getPlayerId() == playerId]

    def checkDice(self, playerId):
        for dice in self.__dicelist:
            if dice.getPlayerId() == playerId:
                return dice

        return None
