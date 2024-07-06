from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.controller.views import OrderView

router = DefaultRouter()
router.register(r'orders', OrderView, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
    path('create', OrderView.as_view({'post': 'createOrders'}), name='order-create'),
    path('read/<int:orderId>', OrderView.as_view({'post': 'readOrders'}), name='order-read'),
]