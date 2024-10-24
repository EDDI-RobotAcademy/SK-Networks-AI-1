from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from ai_request.service.ai_request_service_impl import AiRequestServiceImpl
from backlog_issue.service.backlog_issue_service_impl import BacklogIssueServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl



class AiRequestView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    AiRequestService = AiRequestServiceImpl.getInstance()

    def aiRequestToFastAPI(self, request):
        data = request.data
        userToken = data.get('userToken')
        data = data.get('data')

        requestComplete = self.AiRequestService.aiRequestToFastAPI(userToken, data)

        return Response(requestComplete, status=status.HTTP_200_OK)
