from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backlog_domain.controller.views import BacklogDomainView

router = DefaultRouter()
router.register(r'backlog_todo_check', BacklogDomainView, basename='backlog-todo-check')

urlpatterns = [
    path('', include(router.urls)),
    path('create', BacklogDomainView.as_view({'post': 'createBacklogTodoCheck'}), name='create-backlog-todo-check'),
]
