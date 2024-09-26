from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backlog_domain.controller.views import BacklogDomainView

router = DefaultRouter()
router.register(r'backlog_domain', BacklogDomainView, basename='backlog-domain')

urlpatterns = [
    path('', include(router.urls)),
    path('create', BacklogDomainView.as_view({'post': 'createBacklogDomain'}), name='create-domain'),
]
