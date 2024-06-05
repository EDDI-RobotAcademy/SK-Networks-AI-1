from abc import ABC, abstractmethod


class GameService(ABC):
    @abstractmethod
    def playGame(self, firstPlayer, secondPlayer):
        pass

    @abstractmethod
    def findWinner(self, firstPlayer, secondPlayer):
        pass
