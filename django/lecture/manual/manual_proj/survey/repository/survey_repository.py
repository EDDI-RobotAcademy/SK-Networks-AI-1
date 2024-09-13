from abc import ABC, abstractmethod


class SurveyRepository(ABC):
    @abstractmethod
    def create(self, title, description):
        pass

    @abstractmethod
    def findSurveyById(self, survey_id):
        pass
