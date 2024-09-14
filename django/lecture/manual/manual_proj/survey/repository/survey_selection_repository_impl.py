from django.db import IntegrityError

from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_selection import SurveySelection
from survey.repository.survey_selection_repository import SurveySelectionRepository


class SurveySelectionRepositoryImpl(SurveySelectionRepository):
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

    def createSurveySelection(self, question, selection_text):
        if not isinstance(question, SurveyQuestion):
            raise ValueError("Question must be an instance of SurveyQuestion")

        try:
            selection = SurveySelection(question=question, selection_text=selection_text)
            selection.save()
            return selection

        except IntegrityError as e:
            raise IntegrityError(f"Error creating survey selection: {e}")
