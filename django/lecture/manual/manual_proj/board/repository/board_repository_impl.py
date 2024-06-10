from board.entity.models import Board
from board.repository.board_repository import BoardRepository


class BoardRepositoryImpl(BoardRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        print(f"list() -> Board", Board)
        print(f"list() -> Board.objects", Board.objects)
        print(f"list() -> Board.objects.all()", Board.objects.all())

        boardList = Board.objects.all()
        for board in boardList:
            print(f"Board: {board}")

        return Board.objects.all()

    def create(self, boardData):
        board = Board(**boardData)
        board.save()
        return board


