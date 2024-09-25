from abc import ABC, abstractmethod

from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_selection import SurveySelection


class SurveySelectionRepository(ABC):

    @abstractmethod
    def createSurveySelection(self, question: SurveyQuestion, selection_text: str) -> SurveySelection:
        pass
