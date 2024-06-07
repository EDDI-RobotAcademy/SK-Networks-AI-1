from abc import ABC, abstractmethod

class GameRepository(ABC):
    @abstractmethod
    def getWinner(self, firstdice, firstplayer, seconddice, secondplayer):
        pass