# (Controller : 외부의 요청을 처리) == (View : 본다 >> 눈으로 보는 것을 처리)
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from board.entity.models import Board
from board.serializers import BoardSerializer
from board.service.board_service_impl import BoardServiceImpl


# viewsets를 사용하려면 rest_framework가 설치되어야 합니다.
# pip install dgangorestframework
class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all() # 보드가 어떻게 되어있든 난 다 조회할거야
    boardService = BoardServiceImpl.getInstance()

    def list(self, request):
        boardList = self.boardService.list()
        serializer = BoardSerializer(boardList, many=True)
        return Response(serializer.data)