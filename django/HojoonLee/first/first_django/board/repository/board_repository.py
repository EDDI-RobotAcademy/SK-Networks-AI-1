from abc import ABC, abstractmethod
class BoardRepository(ABC):

    @staticmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, boardData):
        pass