from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ai_request.controller.views import AiRequestView

router = DefaultRouter()
router.register(r'ai_request', AiRequestView, basename='ai-request')

urlpatterns = [
    path('', include(router.urls)),
    path('send', AiRequestView.as_view({'post': 'aiRequestToFastAPI'}), name='ai-request-to-fastapi'),
]
