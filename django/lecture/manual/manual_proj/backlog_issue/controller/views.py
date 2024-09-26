from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_issue.service.backlog_issue_service_impl import BacklogIssueServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl



class BacklogIssueView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    backlogIssueService = BacklogIssueServiceImpl.getInstance()

    def createBacklogIssue(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        issue = data.get('issue')

        createdBacklogIssue = self.backlogIssueService.createBacklogIssue(backlogId, issue)

        return Response(createdBacklogIssue, status=status.HTTP_200_OK)

    def modifyBacklogIssue(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        domain = data.get('domain')

        modifiedBacklogIssue = self.backlogDomainService.modifyBacklogIssue(backlogId, domain)

        return Response(modifiedBacklogIssue, status=status.HTTP_200_OK)
