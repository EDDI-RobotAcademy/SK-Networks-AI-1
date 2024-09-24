from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backlog_status.controller.views import BacklogStatusView

router = DefaultRouter()
router.register(r'backlog_status', BacklogStatusView, basename='backlog-status')

urlpatterns = [
    path('', include(router.urls)),
    path('create', BacklogStatusView.as_view({'post': 'createBacklogStatus'}), name='create-backlog-status'),
]
