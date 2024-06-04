from abc import ABC, abstractmethod


class GameService(ABC):
    @abstractmethod
    def makeGame(self, nickname):
        pass