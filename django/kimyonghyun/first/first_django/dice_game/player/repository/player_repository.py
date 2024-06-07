from abc import ABC, abstractmethod


class PlayerRepository(ABC):
    @abstractmethod
    def create(self, nickname):
        pass

    @abstractmethod
    def findPlayerByNickname(self, nickname):
        pass

    def list(self):
        pass