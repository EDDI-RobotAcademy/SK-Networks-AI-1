from unittest import TestCase
from unittest.mock import patch, MagicMock

from survey.entity.survey import Survey
from survey.service.survey_service_impl import SurveyServiceImpl

class SurveyServiceTest(TestCase):

    @patch('survey.service.survey_service_impl.SurveyRepositoryImpl')
    def test_create_survey_success(self, MockSurveyRepositoryImpl):
        mockRepository = MockSurveyRepositoryImpl.getInstance.return_value
        mockRepository.create.return_value = True

        SurveyServiceImpl._SurveyServiceImpl__instance = None
        surveyService = SurveyServiceImpl.getInstance()

        result = surveyService.createSurvey("Test Survey", "Test Description")

        self.assertTrue(result)
        mockRepository.create.assert_called_once_with("Test Survey", "Test Description")

    @patch('survey.service.survey_service_impl.SurveyRepositoryImpl')
    def test_create_survey_failure(self, MockSurveyRepositoryImpl):
        mockRepository = MockSurveyRepositoryImpl.getInstance.return_value
        mockRepository.create.return_value = False

        SurveyServiceImpl._SurveyServiceImpl__instance = None
        surveyService = SurveyServiceImpl.getInstance()

        result = surveyService.createSurvey("Test Survey", "Test Description")

        self.assertFalse(result)
        mockRepository.create.assert_called_once_with("Test Survey", "Test Description")
