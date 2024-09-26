from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_domain.service.backlog_domain_service_impl import BacklogDomainServiceImpl
from backlog_todo.service.backlog_todo_service_impl import BacklogTodoServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl



class BacklogTodoView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    backlogTodoService = BacklogTodoServiceImpl.getInstance()

    def createBacklogTodo(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        todo = data.get('todo')

        createdBacklogTodo = self.backlogTodoService.createBacklogTodo(backlogId, todo)

        return Response(createdBacklogTodo, status=status.HTTP_200_OK)

    def modifyBacklogTodo(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        todo = data.get('todo')

        modifiedBacklogTodo = self.backlogTodoService.modifyBacklogDomain(backlogId, todo)

        return Response(modifiedBacklogTodo, status=status.HTTP_200_OK)
