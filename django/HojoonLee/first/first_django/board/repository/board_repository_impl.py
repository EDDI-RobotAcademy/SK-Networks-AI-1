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

        # models.py가 실질적으로 Django 설정과 연결되어 있음
        # 이 부분에 정의된 게시물 객체가 Board에 해당함
        # 즉 DB에서 Board를 표현하는 테이블을 읽어서 그 전체를 반환하는 작업
        return Board.objects.all().order_by('regDate')

    def create(self, boardData):
        # title, writer, content 내용을 토대로 Board 객체를 생성
        # 이 객체는 또한 models.py에 의해 구성된 객체로
        # save()를 수행하는 순간 DB에 기록됨
        board = Board(**boardData) # 테이블에 들어가야 하기때문에 request에 담긴 순수데이터만 뽑겠다. [] {} ""
        board.save() # baord => 현재 table 상태입니다.
        return board

    def findByBoardId(self, boardId):
        # boardId를 입력된 boardId로 하겠다는걸 명시하기
        return Board.objects.get(boardId=boardId) # 실제 boardId에 관한 정보를 가져와라 >> 즉, (pk)와 상응하는 객체가 반환됨

    def deleteByBoardId(self, boardId):
        board = Board.objects.get(boardId=boardId) # 일단 삭제할 보드 찾기
        board.delete() # 이미 자체적으로 구현되어있는 delete >> save와 마찬가지 >> django.db의 models에서 자체적으로 지원하는듯
        # django.db model은 crud 중 또 어떤 기능들을 지원할까??

    def update(self, board, boardData):
        for key, value in boardData.items(): # [(key1, value1), ... ,(keyN, valueN)]
            print(f"key: {key}, value: {value}")
            # 쉽게 생각해보자면 board 라는 entity가 가지고 있는 속성값 중
            # 현재 수정 요청에 의해 전달된 정보에 대응되는 key가 가지고 있는 value값을 갱신시킴
            setattr(board, key, value) # modify 기능 완료!
        board.save() # 업뎃된 보드 저장 >> 근데 board는 pk 아닌가? >> findByBoairdID로 객체가 반환되어서 ㄱㅊ함
        return board