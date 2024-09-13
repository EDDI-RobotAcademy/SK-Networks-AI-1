from unittest import TestCase
from unittest.mock import patch, MagicMock
from survey.entity.survey import Survey
from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_type import SurveyType
from survey.repository.survey_question_repository_impl import SurveyQuestionRepositoryImpl


class SurveyQuestionRepositoryTest(TestCase):

    @patch('survey.repository.survey_question_repository_impl.SurveyQuestion')
    @patch('survey.repository.survey_question_repository_impl.SurveyQuestionRepositoryImpl')
    def test_create_survey_question_success(self, MockSurveyQuestionRepositoryImpl, MockSurveyQuestion):
        mock_repository = MockSurveyQuestionRepositoryImpl.return_value

        mock_survey = MagicMock(Survey)

        mock_question = MockSurveyQuestion.return_value
        mock_question.survey = mock_survey
        mock_question.question_text = "What is your opinion on AI?"
        mock_question.survey_type = SurveyType.GENERAL
        mock_repository.create.return_value = mock_question

        survey_question_repository = SurveyQuestionRepositoryImpl()
        result = survey_question_repository.create(mock_survey, "What is your opinion on AI?", SurveyType.GENERAL)

        self.assertTrue(result)

    @patch('survey.repository.survey_question_repository_impl.SurveyQuestionRepositoryImpl')
    def test_create_survey_question_failure(self, MockSurveyQuestionRepositoryImpl):
        mock_repository = MockSurveyQuestionRepositoryImpl.return_value
        mock_repository.create.side_effect = ValueError("Survey must be an instance of Survey")
        survey_question_repository = SurveyQuestionRepositoryImpl()

        with self.assertRaises(ValueError):
            survey_question_repository.create(None, "What is your opinion on AI?", SurveyType.GENERAL)
