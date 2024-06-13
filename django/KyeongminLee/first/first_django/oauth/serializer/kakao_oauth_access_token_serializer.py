from rest_framework import serializers

class KakaoOauthAccessTokenSeriailzer(serializers.Serializer):
    code = serializers.CharField()