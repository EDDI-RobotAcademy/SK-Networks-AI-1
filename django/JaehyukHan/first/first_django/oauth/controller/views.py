from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from oauth.service.oauth_service_impl import OauthServiceImpl
from oauth.serializer.kakao_oauth_url_serializer import KakaoOauthUrlSerializer

# Create your views here.
# Google OAuth 등이 있으므로 사실 Kakao OAuth라고 하는 것이 더 좋았을 것 같음
class OauthView(viewsets.ViewSet):
    oauthService = OauthServiceImpl.getInstance()

    # 사용자가 '카카오 로그인' 버튼을 눌러 요청 시 로그인 경로를 리턴
    def kakaoOauthURI(self, request):
        url = self.oauthService.kakaoLoginAddress()
        serializer = KakaoOauthUrlSerializer(data={ 'url': url })
        serializer.is_valid(raise_exception=True)
        print(f"validated_data: {serializer.validated_data}")
        return Response(serializer.validated_data)
