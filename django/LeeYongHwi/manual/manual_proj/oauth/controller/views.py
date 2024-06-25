import uuid

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl
from oauth.serializer.kakao_oauth_access_token_serializer import KakaoOauthAccessTokenSerializer
from oauth.serializer.kakao_oauth_url_serializer import KakaoOauthUrlSerializer
from oauth.service.oauth_service_impl import OauthServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl

# Google OAuth 등이 있으므로 사실 Kakao OAuth라고 하는 것이 더 좋았을 것 같음
# 패키지 이름 kakaoOauth <-> oauth
class OauthView(viewsets.ViewSet):
    oauthService = OauthServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()

    # 사용자가 '카카오 로그인' 버튼을 눌러 요청시 로그인 경로를 리턴
    def kakaoOauthURI(self, request):
        url = self.oauthService.kakaoLoginAddress()
        print(f"url:", url)
        serializer = KakaoOauthUrlSerializer(data={ 'url': url })
        serializer.is_valid(raise_exception=True)
        print(f"validated_data: {serializer.validated_data}")
        return Response(serializer.validated_data)

    def kakaoAccessTokenURI(self, request):
        serializer = KakaoOauthAccessTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']

        try:
            accessToken = self.oauthService.requestAccessToken(code)
            print(f"accessToken: {accessToken}")
            return JsonResponse({'accessToken': accessToken})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def kakaoUserInfoURI(self, request):
        accessToken = request.data.get('access_token')
        print(f'accessToken: {accessToken}')

        try:
            user_info = self.oauthService.requestUserInfo(accessToken)
            return JsonResponse({'user_info': user_info})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def redisAccessToken(self, request):
        try:
            email = request.data.get('email')
            # TODO: 처음에 좀 비몽사몽한 상태로 만들어서 쓸대없이 accessToken 넣었으나 필요 없음
            #       향후 로직에서 제거할 필요가 있음 (일단 되게 만들기)
            #       토큰 탈취 시 카카오 계정까지 털려버림
            access_token = request.data.get('accessToken')
            print(f"redisAccessToken -> email: {email}")
            print(request.data.get('nickname'))

            account = self.accountService.findAccountByEmail(email)
            if not account:
                return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

            userToken = str(uuid.uuid4())
            self.redisService.store_access_token(account.id, userToken)

            return Response({ 'userToken': userToken }, status=status.HTTP_200_OK)
        except Exception as e:
            print('Error storing access token in Redis:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def dropRedisTokenForLogout(self, request):
        try:
            userToken = request.data.get('userToken')
            isSuccess = self.redisService.deleteKey(userToken)

            return Response({'isSuccess': isSuccess}, status=status.HTTP_200_OK)
        except Exception as e:
            print("레디스 토큰 해제 중 에러 발생", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)