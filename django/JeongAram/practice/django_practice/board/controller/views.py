# Controller : 외부의 요청을 처리 == Views : 눈으로 보는 것을 처리
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from board.entity.models import Board
from board.serializers import BoardSerializer
from board.service.board_service_impl import BoardServiceImpl
# Create your views here.
# viewsets를 사용하려면 rest_framework가 설정되어야 합니다.
# pip install djangorestframework
class BoardView(viewsets.ViewSet):  # CRUD에 있어서 코드관리와 편의성 위주인것 같음
    queryset = Board.objects.all()  # 이렇게 선언해줘야 Board Entity가 db처럼 사용가능(중요) -- 권한을 준다고 이해
    # entity class가 save, delete를 사용할 수 있고, id 입력주면 관련된 데이터들을 겟할 수 있도록 해줌

    boardService = BoardServiceImpl.getInstance() # 외부요청을 Service로 보내기 위함
    # 1단계 하단에 보내기 위해서 징검다리(통로)가 필요한데 이 통로 역할을 getInstance()가 해준다.

    def list(self, request):  # controller는 외부요청(vue요청)을 다루기 떄문에 함수 입력인자로 request를 포함한다.
        boardList = self.boardService.list()
        print('boardList:', boardList)
        serializer = BoardSerializer(boardList, many=True)
        print('serialized boardList:', serializer.data)
        return Response(serializer.data)
    def create(self, request):
        # serializer 왜 쓰는지 ?
        serializer = BoardSerializer(data=request.data)  # 어떤 데이터를 받기 위함인지 명시적으로 받기 위함
        if serializer.is_valid():
            board = self.boardService.createBoard(serializer.validated_data) # 저장이 적용된 테이블 상태
            return Response(BoardSerializer(board).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def read(self, request, pk=None):
        board = self.boardService.readBoard(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)
    def removeBoard(self, request, pk=None):
        self.boardService.removeBoard(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)  # 내용이 없다고 알려주기 반환

    def modifyBoard(self, request, pk=None):
        board = self.boardService.readBoard(pk)  #  해당 게시글 id와 상응하는 게시글 낱개 정보 가져오기
        # board 전체가 아니라 제목, 내용만 가져올거라 request, data로 명시해서 가져오기
        serializer = BoardSerializer(board, data=request.data, partial=True) # 부분적으로 가져올거라 partial True

        if serializer.is_valid():
            # 시리얼라이저 유효하다면 해당 pk 번호의 유용한 데이터(내용, 정보)를 업데이트한다.
            updatedBoard = self.boardService.updateBoard(pk, serializer.validated_data)
            return Response(BoardSerializer(updatedBoard).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)