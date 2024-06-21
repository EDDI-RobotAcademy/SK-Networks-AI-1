from board.repository.board_repository_impl import BoardRepositoryImpl
from board.service.board_service import BoardService
class BoardServiceImpl(BoardService):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # cls.__instance == 현재의 자기자신 클래스 -> BoardServiceImpl
            # class이름.변수 == 그 클래스의 변수 -> 해당 클래스의 종속되어 있는 변수(=멤버 변수)
            # class이름.함수() == 그 클래스의 함수 -> 해당 클래스의 종속되어 있는 함수(=멤버 함수)
            cls.__instance.__boardRepository = BoardRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None: # 한번도 생성하지 않았다면
            cls.__instance = cls() # 새로운 (해당 class) 객체를 만들어주겠습니다.
        return cls.__instance # 해당 클래스 객체가 반환

    def list(self):
        return self.__boardRepository.list()
    def createBoard(self, boardData):
        return self.__boardRepository.create(boardData)
    def readBoard(self, boardId):
        return self.__boardRepository.findByBoardId(boardId)
    def removeBoard(self, boardId):
        return self.__boardRepository.deleteByBoardId(boardId)

    def updateBoard(self, boardId, boardData):
        board = self.__boardRepository.findByBoardId(boardId)
        return self.__boardRepository.update(board, boardData)
