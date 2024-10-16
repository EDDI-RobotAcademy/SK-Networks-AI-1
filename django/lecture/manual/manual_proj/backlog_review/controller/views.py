from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_review.service.backlog_review_service_impl import BacklogReviewServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl



class BacklogReviewView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    backlogReviewService = BacklogReviewServiceImpl.getInstance()

    def createBacklogReview(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        review = data.get('review')

        createdBacklogReview = self.backlogReviewService.createBacklogReview(backlogId, review)

        return Response(createdBacklogReview, status=status.HTTP_200_OK)

    def modifyBacklogReview(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        review = data.get('review')

        modifiedBacklogReview = self.backlogReviewService.modifyBacklogReview(backlogId, review)

        return Response(modifiedBacklogReview, status=status.HTTP_200_OK)
