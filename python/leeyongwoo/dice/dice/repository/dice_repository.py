from abc import ABC, abstractmethod


class DiceRepository(ABC):
    #ABC는 ABstract Class의 약자
    #추상 클래스라는 의미를 가지고 있어서 java 인터페이스 역할과 완벽하게 일치
    #결론적으로 제어 흐름을 인터페이스로 집중 시키는 
    @abstractmethod
    def rollDice(self, playerId):
        pass

    @abstractmethod
    def getDiceNumber(self, playerId):
        pass

    @abstractmethod
    def checkDice(self, playerId):
        pass

    