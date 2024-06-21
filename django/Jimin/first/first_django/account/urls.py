from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.controller.views import AccountView

router = DefaultRouter()
# Entity가 없는 경우 controller에서 직접 querset을 설정 할 수 없으
# 그런 경우 아래와 같이 basename에 패키지를 지정하여 알려줘야함
router.register(r'account', AccountView, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('email-duplication-check', AccountView.as_view({'post': 'checkEmailDuplication'}), name='account-email-duplication-check'),
    path('nickname-duplication-check', AccountView.as_view({'post': 'checkNicknameDuplication'}), name='account-nickname-duplication-check'),
    path('register', AccountView.as_view({'post': 'registerAccount'}), name='register-account'),
]

# localhost:8000/board/list