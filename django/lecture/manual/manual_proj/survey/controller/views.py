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

    def createSurveyQuestion(self, request):
        data = request.data
        survey_id = data.get('survey_id')
        question_text = data.get('question')
        survey_type = data.get('survey_type')

        if not survey_id or not question_text:
            return Response({"error": "설문 ID와 질문 내용이 필요합니다"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            self.surveyService.createSurveyQuestion(survey_id, question_text, survey_type)
            return Response({"success": "질문이 추가되었습니다"}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def createSurveySelection(self, request):
        try:
            data = request.data
            question_id = data.get('question_id')
            selection_text = data.get('selection_text')

            if not question_id or not selection_text:
                return Response({"error": "Question ID and selection text are required."},
                                status=status.HTTP_400_BAD_REQUEST)

            selection = self.surveyService.createSurveySelection(question_id, selection_text)

            return Response({"message": "Selection created successfully", "selection_id": selection.id},
                            status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": "Something went wrong while creating the selection."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

