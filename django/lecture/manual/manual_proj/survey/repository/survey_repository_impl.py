from django.core.paginator import Paginator
from django.db import IntegrityError

from survey.entity.survey import Survey
from survey.entity.survey_status import SurveyStatus
from survey.repository.survey_repository import SurveyRepository


class SurveyRepositoryImpl(SurveyRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, title, description):
        try:
            survey = Survey(title=title, description=description, status=SurveyStatus.PENDING)
            survey.save()

            return survey

        except IntegrityError:
            return None

    def findById(self, survey_id):
        try:
            return Survey.objects.get(id=survey_id)
        except Survey.DoesNotExist:
            return None
