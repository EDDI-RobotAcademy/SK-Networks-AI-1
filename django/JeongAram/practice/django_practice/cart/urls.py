from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cart.controller.views import CartView
router = DefaultRouter()
router.register(r'cart', CartView, basename='cart')
urlpatterns = [
    path('', include(router.urls)),
    # list를 post로 보내는 이유는 userToken을 위한 보안 때문임
    path('list', CartView.as_view({'post': 'cartItemList'}), name='cart-list'),
    # register는 post 요청이고 이를 수신하면 views.py에 있는 create()을 구동함
    path('register', CartView.as_view({'post': 'cartRegister'}), name='cart-register'),
    path('remove', CartView.as_view({'post': 'cartRemove'}), name='cart-remove'),
]


