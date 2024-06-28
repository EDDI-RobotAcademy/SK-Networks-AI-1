from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cart.controller.views import CartView

router = DefaultRouter()
router.register(r'cart', CartView, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('list', CartView.as_view({'post': 'cartItemList'}), name='cart-list'), #list는 사용자 토큰이 노출되면 안되기 때문에 post로 보낸다.
    path('register', CartView.as_view({'post': 'cartRegister'}), name='cart-register'),
    path('remove', CartView.as_view({'post': 'cartRemove'}), name='cart-remove'),
]

# localhost:8000/board/list