from abc import ABC, abstractmethod


class DiceRepository(ABC):
    # ABC 는 ABstract Class 의 약자입니다 추상 클래스라는 의미를
    # 가지고 있어서 java 인터페이스 역할과 완벽하게 일치합니다.
    # 결론적으로 제어 흐름을 인터페이스로 입중시키는 역할이 핵심이다.
    # IoC 를 달성하기 위한 클래스다.

    @abstractmethod
    def rollDice(self, playerId):
        pass

    @abstractmethod
    def getDiceNumber(self, playerId):
        pass

    @abstractmethod
    def checkDice(self, playerId):
        pass