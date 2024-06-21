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
        # models.py가 실질적으로 Django 설정과 연결되어 있음
        # 이 부분에 정의된 게시물 객체가 Board에 해당함
        # 즉 DB에서 Board를 표현하는 테이블을 읽어서 그 전체를 반환하는 작업
        return Board.objects.all().order_by('-regDate')

    def create(self, boardData):
        # title, writer, content 내용을 토대로 Board 객체를 생성
        # 이 객체는 또한 models.py에 의해 구성된 객체로
        # save()를 수행하는 순간 DB에 기록됨
        board = Board(**boardData) # 내부에 있는거 다 불러온다.
        board.save()
        return board

    def findByBoardId(self, boardId):
        return Board.objects.get(boardId=boardId)
    # boardId의 모든 정보를 불러온다는 뜻 objects가 모든 정보라는 뜻

    def deleteBoardId(self, boardId):
        board = Board.objects.get(boardId=boardId)
        board.delete()

    def update(self, board, boardData):
        for key, value in boardData.items():
            # board라는 entity가 가지고 있는 속성값중 현새 수정 요청에 의해 전달된 정보에 대응되는 key가 가지고 있는 value 값을 갱신
            setattr(board, key, value)

        board.save()
        return board





