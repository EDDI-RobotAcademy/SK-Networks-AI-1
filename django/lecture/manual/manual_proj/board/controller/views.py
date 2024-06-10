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
    queryset = Board.objects.all()
    boardService = BoardServiceImpl.getInstance()

    def list(self, request):
        boardList = self.boardService.list()
        print('boardList:', boardList)
        serializer = BoardSerializer(boardList, many=True)
        print('serialized boardList:', serializer.data)
        return Response(serializer.data)

    def create(self, request):
        serializer = BoardSerializer(data=request.data)

        if serializer.is_valid():
            board = self.boardService.createBoard(serializer.validated_data)
            return Response(BoardSerializer(board).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
