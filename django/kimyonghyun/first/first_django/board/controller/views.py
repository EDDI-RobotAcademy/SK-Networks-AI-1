from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from board.entity.models import Board
from board.serializer  import BoardSerializer
from board.service.board_service_impl import BoardServiceImpl
# Create your views here.
# viewsets를 사용하려면 rest_framework가 설정되어야 합니다.

class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all()
    boardService = BoardServiceImpl.getInstance()

    def list(self,request):
        boardlist = self.boardService.list()
        serializer = BoardSerializer(boardlist, many=True)
        return Response(serializer.data)
