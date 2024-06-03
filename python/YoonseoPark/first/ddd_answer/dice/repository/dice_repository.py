from abc import ABC, abstractmethod
# python에서 IoC하는 방법 => ABC
class DiceRepository(ABC):
    @abstractmethod
    def rollDice(self, playerId):
        pass

    @abstractmethod
    def getDiceNumber(self, playerId):
        pass

    @abstractmethod
    def checkDice(self, playerId):
        pass

