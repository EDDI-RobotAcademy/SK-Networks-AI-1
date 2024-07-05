from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders.controller.views import OrdersView

router = DefaultRouter()
router.register(r'orders', OrdersView, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
    path('create', OrdersView.as_view({'post': 'createOrders'}), name='order-create'),
    path('read/<int:orderId>', OrdersView.as_view({'post': 'readOrders'}), name='order-read'),
    path('list', OrdersView.as_view({'post': 'ordersList'}), name='order-list'),
]
