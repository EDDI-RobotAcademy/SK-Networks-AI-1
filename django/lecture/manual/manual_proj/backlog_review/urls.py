from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backlog_review.controller.views import BacklogReviewView

router = DefaultRouter()
router.register(r'backlog_review', BacklogReviewView, basename='backlog-review')

urlpatterns = [
    path('', include(router.urls)),
    path('create', BacklogReviewView.as_view({'post': 'createBacklogReview'}), name='create-backlog-review'),
]
