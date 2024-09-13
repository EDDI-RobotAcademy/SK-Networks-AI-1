from abc import ABC, abstractmethod


class SurveyRepository(ABC):
    @abstractmethod
    def create(self, title, description):
        pass
