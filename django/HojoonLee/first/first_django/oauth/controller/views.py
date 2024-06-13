from rest_framework import viewsets
from rest_framework.response import Response

from oauth.serializer.kakao_oauth_url_serializer import KakaoOauthUrlSerializer
from oauth.service.oauth_service_impl import OauthServiceImpl

class OauthView(viewsets.ViewSet):
    oauthService = OauthServiceImpl.getInstance()

    # 사용자가 '카카오 로그인' 버튼을 눌러(뷰에서) 요청시 로그인 경로를 리턴 (장고에서)
    # 누가 누구한테 보낼 것인지 명확히 해야함 (fast api갈게 django로 요청이 가면 안됨) >> 백로그
    def kakaoOauthURI(self, request): # uri : identifier (요쳥하는 역할을 하기 때문)
        url = self.oauthService.kakaoLoginAddress()
        serializer = KakaoOauthUrlSerializer(data={'url':url}) # 대문자 k임
        serializer.is_valid(raise_exception=True) # vue에서 kakao login 버튼을 누르면 요청이 오고 여기에 대해 redirection
        print(f"validated_data: {serializer.validated_data}")
        return Response(serializer.validated_data)