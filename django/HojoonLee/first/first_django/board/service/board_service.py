from abc import ABC, abstractmethod
class BoardService(ABC):
    # controller에 있던 함수는 list뿐이므로 여기도 list 기능만 구현
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createBoard(self, boardData):
        pass

    @abstractmethod
    def readBoard(self, boardId):
        pass