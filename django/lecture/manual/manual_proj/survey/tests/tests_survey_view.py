from unittest import TestCase
from unittest.mock import patch, MagicMock

from survey.entity.survey import Survey
from survey.service.survey_service_impl import SurveyServiceImpl

class SurveyServiceTest(TestCase):

    @patch('survey.service.survey_service_impl.SurveyRepositoryImpl')
    def test_create_survey_success(self, MockSurveyRepositoryImpl):
        mockSurvey = MagicMock(spec=Survey)
        mockSurvey.title = "Test Survey"
        mockSurvey.description = "Test Description"

        mockRepository = MockSurveyRepositoryImpl.getInstance.return_value
        mockRepository.create.return_value = mockSurvey

        SurveyServiceImpl._SurveyServiceImpl__instance = None
        surveyService = SurveyServiceImpl.getInstance()

        result = surveyService.createSurvey("Test Survey", "Test Description")

        self.assertEqual(result, mockSurvey)
        mockRepository.create.assert_called_once_with("Test Survey", "Test Description")

    @patch('survey.service.survey_service_impl.SurveyRepositoryImpl')
    def test_create_survey_failure(self, MockSurveyRepositoryImpl):
        mockRepository = MockSurveyRepositoryImpl.getInstance.return_value
        mockRepository.create.return_value = None

        SurveyServiceImpl._SurveyServiceImpl__instance = None
        surveyService = SurveyServiceImpl.getInstance()

        result = surveyService.createSurvey("Test Survey", "Test Description")

        self.assertIsNone(result)
        mockRepository.create.assert_called_once_with("Test Survey", "Test Description")
