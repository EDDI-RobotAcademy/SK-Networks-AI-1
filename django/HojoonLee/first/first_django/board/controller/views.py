# (Controller : 외부의 요청을 처리) == (View : 본다 >> 눈으로 보는 것을 처리)
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from board.entity.models import Board
from board.serializers import BoardSerializer
from board.service.board_service_impl import BoardServiceImpl


# viewsets를 사용하려면 rest_framework가 설치되어야 합니다.
# pip install dgangorestframework
class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all() # 이렇게 선언해줘야 Board Entity가 db처럼 사용가능 (중요)
    # entity class가 save, delete를 사용할 수있고, id 입력주면 관련된 데이터들을 get할 수 있도록 해줌
    boardService = BoardServiceImpl.getInstance()

    def list(self, request):
        boardList = self.boardService.list()
        serializer = BoardSerializer(boardList, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BoardSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            board = self.boardService.createBoard(serializer.validated_data)
            return Response(BoardSerializer(board).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        board = self.boardService.readBoard(pk) # 낱개 정보를 가져오기
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def removeBoard(self, request, pk=None):
        self.boardService.removeBoard(pk)
        return Response(status=status.HTTP_204_NO_CONTENT) # 내용이 없다고 알려주기 반환

    def modifyBoard(self, request, pk=None):
        board = self.boardService.readBoard(pk) # 게시글 낱개 정보 가져오기
        # board 전체가 아니라 제목,내용만 가져올거라 request.data로 명시해서 가져오기
        serializer = BoardSerializer(board, data=request.data, partial=True) # 부분적으로 가져올거라 partial True

        if serializer.is_valid():
            # 시리얼라이저 유효하다면 해당 pk 번호의 유용한 데이터(내용, 정보)를 업데이트한다.
            # 반환 받았으니 업뎃된 데이터
            updatedBoard = self.boardService.updateBoard(pk, serializer.validated_data)
            return Response(BoardSerializer(updatedBoard).data) # 잘 가져왔다면 업뎃된 데이터 반환

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 못 가져왔다면 에러 반환