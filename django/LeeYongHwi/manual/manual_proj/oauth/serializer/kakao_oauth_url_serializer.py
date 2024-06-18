from rest_framework import serializers


# Spring으로 보자면 DTO라고 봐도 무방하긴함
# 근데 우리의 경우 원래 Response 혹은 Request로 분류하고 있어서
# 이런 부분의 제약이 약간 아쉬운 부분임
class KakaoOauthUrlSerializer(serializers.Serializer):
    url = serializers.URLField()
