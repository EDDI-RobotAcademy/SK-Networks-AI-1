from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backlog_success_criteria.controller.views import BacklogSuccessCriteriaView

router = DefaultRouter()
router.register(r'backlog_success_criteria', BacklogSuccessCriteriaView, basename='backlog-success-criteria')

urlpatterns = [
    path('', include(router.urls)),
    path('create', BacklogSuccessCriteriaView.as_view({'post': 'createBacklogSuccessCriteria'}), name='create-backlog-success-criteria'),
]
