from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cart.controller.views import CartView

router = DefaultRouter()
router.register(r'cart', CartView, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    # 유저정보 담겨있어서 list도 post로 받는다.
    path('list', CartView.as_view({'post': 'cartItemList'}), name='cart-list'),
    path('register', CartView.as_view({'post': 'cartRegister'}), name='cart-register'),
    path('remove', CartView.as_view({'post': 'cartRemove'}), name='cart-remove'),
]