from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.controller.views import ProductView
router = DefaultRouter()
router.register(r'product', ProductView)
urlpatterns = [
    path('', include(router.urls)),
    # 어떤 경로 요청이 GET 혹은 POST로 있을 경우,
    # as_view({}) 내의 맨 뒤쪽 list 혹은 create 형태가 동작
    # 결론적으로 list는 get 요청으로 오고 이것을 수신하면 controller/views.py 에 있는 list()를 구동함
    path('list/', ProductView.as_view({'get': 'list'}), name='product-list'),
    # register는 post 요청이고 이를 수신하면 views.py에 있는 create()을 구동함
    path('register', ProductView.as_view({'post': 'create'}), name='product-register'),
    path('read/<int:pk>', ProductView.as_view({'get': 'read'}), name='product-read'),
    path('delete/<int:pk>', ProductView.as_view({'delete': 'removeProduct'}), name='product-remove'),
    path('modify/<int:pk>', ProductView.as_view({'put': 'productBoard'}), name='product-modify'),
    path('modify/<int:pk>', ProductView.as_view({'put': 'productBoard'}), name='product-modify'),
]

# localhost:8000/board/list