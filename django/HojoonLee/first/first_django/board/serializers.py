from rest_framework import serializers
from board.entity.models import Board

# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다.
#
class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board # Board 참고한다.
        fields = ['board', 'title', 'writer', 'content', 'regDate', 'updDate'] # 내가 models에서 쿼리 날린것들
        read_only_fields = ['regDate', 'updDate']