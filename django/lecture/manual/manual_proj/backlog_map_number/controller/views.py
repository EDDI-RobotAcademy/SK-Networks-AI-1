from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_map_number.service.backlog_map_number_service_impl import BacklogMapNumberServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl



class BacklogMapNumberView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    backlogMapNumberService = BacklogMapNumberServiceImpl.getInstance()

    def createBacklogDomain(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        backlogMapNumber = data.get('backlog_map_number')

        createdBacklogDomain = self.backlogMapNumberService.createBacklogMapNumber(backlogId, backlogMapNumber)

        return Response(createdBacklogDomain, status=status.HTTP_200_OK)

    def modifyBacklogDomain(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        backlogMapNumber = data.get('backlog_map_number')

        modifiedBacklogDomain = self.backlogMapNumberService.modifyBacklogMapNumber(backlogId, backlogMapNumber)

        return Response(modifiedBacklogDomain, status=status.HTTP_200_OK)
