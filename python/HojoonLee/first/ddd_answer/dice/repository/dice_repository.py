# abstractmethod (자바의 인터페이스 기능)
# 으름장 놓는 기능 >> 나 이런거할건데 어떻게 생각해?
# 이걸 파이썬 상에서 해주는게 IoC 를 통해서..
# 제어역전(IoC) : 특정 메서드 변경에 의해 다른 곳에서의 오류의 파급효과를 최소화 시키기 위함
# 터져도 IoC 역할을 하는 인터페이스만 터진다.
# https://cafe.naver.com/eddicorp/2097

from abc import ABC, abstractmethod
class DiceRepository(ABC):
    # ABC는 ABstract Class의 약자
    # 추상 클래스라는 의미를 가지고 있어서 java 인터페이스 역할과 완벽하게 일치합니다.
    # 결론적으로 제어흐름을 인터페이스로 집중 시키는 역할이 핵심입니다.
    # 줄여서 IoC (Inversion of Control)을 달성하기 위한 클래스라고 정리하면 되겠습니다.
    # 여기서 선언한 method들은 반드시 impl에서 구현해야 함 >> 선언만하고 구현안하면 에러 발생
    @abstractmethod
    def rollDice(self, playerId):
        pass

    @abstractmethod
    def getDiceNumber(self, playerId):
        pass

    @abstractmethod
    def checkDice(self, playerId):
        pass
