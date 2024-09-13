from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from oauth.service.redis_service_impl import RedisServiceImpl
from survey.service.survey_service_impl import SurveyServiceImpl


class SurveyView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    surveyService = SurveyServiceImpl.getInstance()

    def createSurvey(self, request):
        data = request.data
        title = data.get('title')
        description = data.get('description')

        if not title:
            return Response({"error": "제목이 필요합니다"}, status=status.HTTP_400_BAD_REQUEST)

        isCreated = self.surveyService.createSurvey(title, description)

        return Response(isCreated, status=status.HTTP_200_OK)

