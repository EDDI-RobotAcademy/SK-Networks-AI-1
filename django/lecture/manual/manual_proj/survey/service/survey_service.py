from abc import ABC, abstractmethod


class SurveyService(ABC):
    @abstractmethod
    def createSurvey(self, title, description):
        pass

    @abstractmethod
    def createSurveyQuestion(self, survey_id, question_text, survey_type):
        pass

    @abstractmethod
    def createSurveySelection(self, question_id, selection_text):
        pass
