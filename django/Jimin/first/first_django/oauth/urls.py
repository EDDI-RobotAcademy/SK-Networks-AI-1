from django.urls import path, include
from rest_framework.routers import DefaultRouter

from oauth.controller.views import OauthView

router = DefaultRouter()
# Entity가 없는 경우 controller에서 직접 querset을 설정 할 수 없으
# 그런 경우 아래와 같이 basename에 패키지를 지정하여 알려줘야함
router.register(r'oauth', OauthView, basename='oauth')

urlpatterns = [
    path('', include(router.urls)),
    path('kakao', OauthView.as_view({'get': 'kakaoOauthURI'}), name='get-kakao-oauth-uri'),
    path('kakao/access-token', OauthView.as_view({'post': 'kakaoAccessTokenURI'}), name='get-kakao-access-token-uri'),
    path('kakao/user-info', OauthView.as_view({'post': 'kakaoUserInfoURI'}), name='get-kakao-user-info-uri'),
    path('redis-access-token/', OauthView.as_view({'post': 'redisAccessToken'}), name='redis-access-token')
]

# localhost:8000/board/list