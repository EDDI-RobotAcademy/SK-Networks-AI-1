from django.shortcuts import render
from rest_framework import viewsets

from first_django.board.entity.models import Board


# Create your views here.
# viewset을 사용하려면 rest_framework가 설정되어야 합니다.
# pip install djangorestframework
class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all()
    boardService = BoardServiceImple.getInstance()

    def list(self, request):
        boardList = self.boardService.list()
        serializer = BoardSerializer(boardList, many=True)
        return Response(serializer.data)

