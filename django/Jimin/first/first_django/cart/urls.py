from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cart.controller.views import CartView

router = DefaultRouter()
router.register(r'cart', CartView, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    # 어떤 경로 요청이 GET 혹은 POST로 있을 경우, as_view({}) 내의 맨 뒤쪽 list 혹은 create 형태가 동작
    # 결론적으로 list는 get 요청으로 오고 이것을 수신하면 controller/views.py에 있는 list()를 구동함
    path('list', CartView.as_view({'post': 'cartItemList'}), name='cart-list'),
    # register는 post 요청이고 이를 수신하면 views.py에 있는 create()을 구동함
    # 사용자 토큰이 외부로 노출되면 안되기 때문에 post 요청
    path('register', CartView.as_view({'post': 'cartRegister'}), name='cart-register'),

]