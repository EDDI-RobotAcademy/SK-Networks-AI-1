from abc import ABC, abstractmethod

class GameRepository(ABC):

    @abstractmethod
    def save(self, playerDiceMap):
        pass

    @abstractmethod
    def checkDiceGameWinner(self):
        pass