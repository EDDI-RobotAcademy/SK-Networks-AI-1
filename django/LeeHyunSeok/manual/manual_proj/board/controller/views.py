from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from board.entity.models import Board
from board.serializers import BoardSerializer
from board.service.board_service_impl import BoardServiceImpl


# Create your views here.
# viewsets를 사용하려면 rest_framework가 설정되어야 합니다.
# pip install djangorestframework
class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all() #이렇게 선언해줘야 Board Entity가 db처럼 사용 가능(중요)
    #엔티티 클래스가 세이브,델리트를 사용할 수 있고, id입렵해 주면 관련된 데이터들을 get할 수 있도록 허용
    boardService = BoardServiceImpl.getInstance() # 외부 요청을 service로 보내기 위함
    # 1단계 하단으로 보내기 위해서 징검다리가 필요한데 이 징검다리 역할을 getInstace()가 해줍니다.
    #혼자 하면 여기까진 무조건 해야하는 절차

    def list(self, request):   #controller는 외부(vue) 요청을 다루기 때문에 함수 입력 인자로 request가 포함된다.
        boardList = self.boardService.list()      #request는 외부에서 들어온 요청을 그대로 담고 있다.
        print('boardList:', boardList)
        serializer = BoardSerializer(boardList, many=True)
        print('serialized boardList:', serializer.data)
        return Response(serializer.data)

    def create(self, request):
        serializer = BoardSerializer(data=request.data) #어떤 데이터인지 명시적으로 받기 위함

        if serializer.is_valid():
            board = self.boardService.createBoard(serializer.validated_data)
            return Response(BoardSerializer(board).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        board = self.boardService.readBoard(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def removeBoard(self, request, pk=None):
        self.boardService.removeBoard(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def modifyBoard(self, request, pk=None):
        board = self.boardService.readBoard(pk) #게시글 낱개 정보 가져오기
        #board 전체가 아니라 제목,내용만 가져올거라 request.data로 명시해서 가져오기
        serializer = BoardSerializer(board, data=request.data, partial=True) #부분적으로 가져올거란 partial True

        if serializer.is_valid():
            #시리얼라이저 유효하다면 해당 pk번호의 유용한 데이터(내용,정보)를 업데이트 한다.
            #반환 받았으니 업뎃된 데이터
            updatedBoard = self.boardService.updateBoard(pk, serializer.validated_data)
            return Response(BoardSerializer(updatedBoard).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)