from abc import ABC, abstractmethod
class BoardRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, boardData):
        pass

    # read 기능 지원
    @abstractmethod
    def findByBoardId(self, boardId):
        pass

    @abstractmethod
    def deleteByBoardId(self, boardId):
        pass

    @abstractmethod
    def update(self, board, boardData):
        pass