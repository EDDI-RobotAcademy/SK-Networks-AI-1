from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'backlog_map_number', BacklogMapNumberView, basename='backlog-map-number')

urlpatterns = [
    path('', include(router.urls)),
    path('create', BacklogMapNumberView.as_view({'post': 'createBacklogMapNumber'}), name='create-backlog-map-number'),
]
