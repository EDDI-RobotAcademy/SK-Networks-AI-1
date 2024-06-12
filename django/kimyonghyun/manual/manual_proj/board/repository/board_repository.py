from abc import ABC, abstractmethod


class BoardRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, boardData):
        pass

    @abstractmethod
    def findByBoardId(self,boardId):
        pass