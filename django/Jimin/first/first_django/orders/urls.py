from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.controller.views import OrdersView

router = DefaultRouter()
router.register(r'orders', OrdersView, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
    path('create', OrdersView.as_view({'post': 'createOrders'}), name='order-create')
]