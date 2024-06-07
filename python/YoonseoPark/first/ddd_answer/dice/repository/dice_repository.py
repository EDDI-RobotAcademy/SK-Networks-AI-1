from abc import ABC, abstractmethod
# python에서 IoC하는 방법 => ABC
class DiceRepository(ABC):
    # ABC는 ABstract Class의 약자입니다.
    # 추상 클래스라는 의미를 가지고 있어서 java 인터페이스 역할과 완벽하게 일치합니다.
    # 결론적으로 제어 흐름을 인터페이스로 집중 시키는 역할이 핵심입니다.
    # 줄여서 IoC (Inversion of Control)을 달성하기 위한 클래스라고 정리하면 되겠습니다.
    @abstractmethod
    def rollDice(self, playerId):
        pass

    @abstractmethod
    def getDiceNumber(self, playerId):
        pass

    @abstractmethod
    def checkDice(self, playerId):
        pass

