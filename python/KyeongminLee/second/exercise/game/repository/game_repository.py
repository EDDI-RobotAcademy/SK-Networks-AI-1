from abc import ABC, abstractmethod

class GameRepository:
    @abstractmethod
    def save(self, playerDiceMap):
        pass

    def checkDiceGameWinner(self):
        pass