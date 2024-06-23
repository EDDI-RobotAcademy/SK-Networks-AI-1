from django.urls import path, include
from rest_framework.routers import DefaultRouter

from travel.controller.views import TravelView

router = DefaultRouter()
router.register(r'travel', TravelView)

urlpatterns = [
    path('', include(router.urls)),
]
