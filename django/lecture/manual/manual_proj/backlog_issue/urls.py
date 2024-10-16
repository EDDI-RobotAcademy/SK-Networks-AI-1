from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backlog_issue.controller.views import BacklogIssueView

router = DefaultRouter()
router.register(r'backlog_issue', BacklogIssueView, basename='backlog-issue')

urlpatterns = [
    path('', include(router.urls)),
    path('create', BacklogIssueView.as_view({'post': 'createBacklogIssue'}), name='create-backlog-issue'),
]
