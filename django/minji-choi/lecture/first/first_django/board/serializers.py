from rest_framework import serializers
from board.entity.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['boardId','title','writer','content','regDate','upDate']
        read_only_fields = ['regDate','upDate']