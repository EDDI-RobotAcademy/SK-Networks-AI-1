from rest_framework import serializers


class KakaoOauthUrlSerializer(serializers.Serializer):
    # queryset 해줘야 하는데 entity가 없는 경우에는 ?
    url = serializers.URLField()

