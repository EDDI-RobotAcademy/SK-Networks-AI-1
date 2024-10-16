from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backlog_map_number.controller.views import BacklogMapNumberView

router = DefaultRouter()
router.register(r'backlog_map_number', BacklogMapNumberView, basename='backlog-map-number')

urlpatterns = [
    path('', include(router.urls)),
    path('create', BacklogMapNumberView.as_view({'post': 'createBacklogMapNumber'}), name='create-backlog-map-number'),
]
