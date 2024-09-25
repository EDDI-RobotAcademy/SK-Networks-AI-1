from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backlog.controller.views import BacklogView

router = DefaultRouter()
router.register(r'backlog', BacklogView, basename='backlog')

urlpatterns = [
    path('', include(router.urls)),
    path('create', BacklogView.as_view({'post': 'createBacklog'}), name='create-backlog'),
]
