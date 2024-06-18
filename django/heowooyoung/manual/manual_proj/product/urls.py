from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.controller.views import ProductView

router = DefaultRouter()
router.register(r'product', ProductView)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', ProductView.as_view({'get': 'list'}), name='product-list'),
    path('register', ProductView.as_view({'post': 'register'}), name='product-register'),
    path('read/<int:pk>', ProductView.as_view({'get': 'readProduct'}), name='product-read'),
]