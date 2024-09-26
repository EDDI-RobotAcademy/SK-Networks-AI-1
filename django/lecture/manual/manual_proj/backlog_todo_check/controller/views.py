from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_domain.service.backlog_domain_service_impl import BacklogDomainServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl



class BacklogTodoCheckView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    backlogTodoCheckService = BacklogTodoCheckServiceImpl.getInstance()

    def createBacklogTodoCheck(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        isChecked = data.get('isChecked')

        createdBacklogTodoCheck = self.backlogTodoCheckService.createBacklogTodoCheck(backlogId, isChecked)

        return Response(createdBacklogTodoCheck, status=status.HTTP_200_OK)

    def modifyBacklogTodoCheck(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        isChecked = data.get('isChecked')

        modifiedBacklogTodoCheck = self.backlogTodoCheckService.modifyBacklogTodoCheck(backlogId, isChecked)

        return Response(modifiedBacklogTodoCheck, status=status.HTTP_200_OK)
