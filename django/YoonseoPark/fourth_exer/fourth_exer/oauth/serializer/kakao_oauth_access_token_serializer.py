from rest_framework import serializers


class KakaoOauthAccessTokenSerializer(serializers.Serializer):
    code = serializers.CharField()