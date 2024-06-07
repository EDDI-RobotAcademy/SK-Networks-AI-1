from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from board.entity.models import Board

# Create your views here.
# viewsets를 사용하려면 rest_framework가 설정되어야 합니다.

class BoardView(viewsets.Viewset):
    queryset = Board.objects.all()
    board_service = BoardServiceImpl.getInstance()

    def list(self, request):
        boardList = self.boardService.list()
        serializer = BoardSerializer(boardList, many = True)

        return Response(serializer.data)

