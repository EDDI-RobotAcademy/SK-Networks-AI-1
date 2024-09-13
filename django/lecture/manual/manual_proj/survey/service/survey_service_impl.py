from account.repository.account_repository_impl import AccountRepositoryImpl
from survey.repository.survey_repository_impl import SurveyRepositoryImpl

from survey.service.survey_service import SurveyService


class SurveyServiceImpl(SurveyService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__surveyRepository = SurveyRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createSurvey(self, title, description):
        try:
            return self.__surveyRepository.create(title, description)

        except Exception as e:
            print('Error creating order:', e)
            raise e
