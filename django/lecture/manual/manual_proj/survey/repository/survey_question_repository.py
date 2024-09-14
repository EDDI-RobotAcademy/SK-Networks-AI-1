from abc import ABC, abstractmethod

class SurveyQuestionRepository(ABC):
    @abstractmethod
    def create(self, survey, question_text, survey_type):
        pass

    @abstractmethod
    def findSurveyQuestionListBySurveyId(self, survey_id):
        pass

    @abstractmethod
    def findById(self, survey_question_id):
        pass

    