# dice repository.py 부분 구현 >> c++로 치면 헤더의 구현부분
import random

from dice.entity.DiceNumber import DiceNumber
from dice.entity.dice import Dice
# from dice.entity import DiceNumber
from dice.repository.dice_repository import DiceRepository
# impl 부분에선 dice_repository.py의 추상화된 부분 구체화 시킴
# 이런 기능을 하겠다!

# 파이썬의 상속은 아래와 같이 class A(상속할 클래스) 형태로 상속을 진행합니다.
# 인터페이스를 상속 받아서 가져온 클래스는 (.header)
# 반드시 인터페이스 클래스에 있는 함수들을 구체적으로 만들어 줘야 합니다. (.cpp)
# 제어의 흐름을 인터페이스가 해주도록 만들어줌 (C에서는 추가적으로 포인터 설정을 해줘야 함)
# 앞으로 instance를 만들어주면 여기 repository 구현 부만 찾게 됨 >> cls.__instance 부분
class DiceRepositoryImpl(DiceRepository):
    # alt + insert로 자동완성하기 (from ~ import 먼저 해줘야 뜸)

    # singletion(싱글톤) 객체를 만들기 위한 기법 시작
    # entity말고 다른 것(repo, service..)들은 객체를 더 만들 필요가 없으므로 이를 싱글톤으로 구성
    # 싱글톤 : 객체를 유일하게 1개로만 만들겠다.
    # 싱글톤이 되면 객체는 유일성을 가지게 됩니다.
    # Entity에 있는 객체들은 여러개가 될 수 있습니다.
    # 반면 이들을 서포트하는 repository, service 객체가 여러게 존재할 필요가 없습니다.
    # 그러므로 이들은 singleton으로 구성하여 유일성을 가지게 만듭니다.
    # 이것은 궁극적으로 메모리라는 자원을 좀 더 효율적으로 사용하는 기법이 됩니다. (객체를 덜 할당 하므로)


    # __instance는 실질적으로 DiceRepository 구현체가 존재하냐 않냐를 보는 부분입니다.
    # 있다면 아래(__new__, getinstance) 함수에서 입력그대로 return, 없다면 만들어서 return
    __instance = None

    # __new__ 를보면 제일 이상한 부분이 보이는데 cls라는 것입니다.
    # 도대체 cls는 무엇일까요?
    # 보편적으로 cls는 클래스와 메서드가 서로 참조하기 위해 사용하는 내부 인자입니다.
    # self랑은 무슨 관계지? 라는 생각이 보편적으로 들 수 있습니다.
    # self는 초기화가 끝나야지만 사용 가능
    # __new__ 를 해야만이 객체 생성(초기화)가 되는데, 여기서 self를 쓸 수 없으므로 이 때 사용하는 것이 cls
    # 이 시점에서 클래스 자체에 접근 할 수 있는 인자가 cls 입니다. (cls == 클래스 자체)
    def __new__(cls):
        if cls.__instance is None: # 한번 만들어진 객체는 계속 유지 >> 싱글톤의 특성
            cls.__instance = super().__new__(cls) # parent class 생성 >> DiceRepository(인터페이스) class
            cls.__instance.__dicelist = []

        return cls.__instance # if문 안에다 return 시켜서 없는 상태에서 반환되어 Nonetype이 됨
    @classmethod
    def getInstance(cls):
        if cls.__instance is None: # 해당 객체가 없다면
            cls.__instance = cls() # 불러온 객체(cls)로 할당

        return cls.__instance
    # Singleton(싱글톤) 객체를 만들기 위한 기법 끝!

    def rollDice(self, playerId):
        diceNumber = random.randint(DiceNumber.ONE.value, DiceNumber.SIX.value)
        # 모두 다 상수가 아닌 변수 화를 위해 DiceNumber.ONE.value 이런 식으로 선언함
        # 빨간줄 alt + enter로 자동 import 해주기
        dice = Dice() # Dice 클래스도 alt + enter로 자동 import >> Dice class 메서드 쓰기 위함
        dice.setDiceNumber(diceNumber)
        dice.setPlayerId(playerId)
        self.__dicelist.append(dice) # 주사위 값, player 정보가 저장
        # print(self.__dicelist) # 할당 됨

    def getDiceNumber(self, playerId):
        # dicelist에 있는 요소들 중 요청한 playerId와 같은 애의 주사위 번호를 반환
        # rollDice를 호출하기 전에 이걸 호출하면 0이 출력 됨
        # []를 씌운 이유는 같은 플레이어가 여러 번 굴리기 때문에 여러 값 넣기 위함
        return [dice.getDiceNumber() for dice in self.__dicelist if dice.getPlayerId() == playerId]

    # 위의 파이썬 style로 작성한 코드를 java(c) style로 다시 풀어 쓰기
    def checkDice(self, playerId):
        # print(self.__dicelist) 뭔가 있는데, if문에 안걸리네..
        for dice in self.__dicelist:
            # print('hihi')
            if dice.getPlayerId() == playerId:
                # print('hi') # 여기 못부름
                return dice
        # print('hello')
        return None # 같은 id가 안 걸렸다면, None 반환