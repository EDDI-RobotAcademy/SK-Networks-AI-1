from abc import ABC,abstractmethod

class GameService(ABC):

    @abstractmethod
    def registerGameResult(self):
        pass
    @abstractmethod
    def checkDiceGameWinner(self):
        pass

