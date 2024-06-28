from rest_framework import serializers


class KakaoOauthUrlSerializer(serializers.Serializer):
    url = serializers.URLField()