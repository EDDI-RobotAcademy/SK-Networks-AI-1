from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from board.entity.models import Board
from board.serializers import BoardSerializer
from board.service.board_service_impl import BoardServiceImpl
# Create your views here.
# viewsets를 사용하려면 rest_framework가 설정되어야 합니다.
# 화면에 보이는 입력을 처리한다?
class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all()
    boardService = BoardServiceImpl.getInstance()

    def list(self, request):
        boardList = self.boardService.list()
        serializer = BoardSerializer(boardList, many=True)
        return Response(serializer.data)
