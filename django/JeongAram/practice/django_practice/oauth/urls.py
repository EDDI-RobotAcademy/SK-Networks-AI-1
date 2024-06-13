from django.urls import path, include
from rest_framework.routers import DefaultRouter

from oauth.controller.views import OauthView

router = DefaultRouter()
router.(r'oauth', OauthView)

urlpatterns = [
    path('', include(router.urls)),
    path('kakao', OauthView.as_view({'get': 'kakaoOauthURI'}), name='get-kakao-oauth-uri'),

]

# localhost:8000/board/list