from unittest import TestCase
from unittest.mock import patch
from survey.entity.survey import Survey
from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_type import SurveyType
from survey.repository.survey_question_repository_impl import SurveyQuestionRepositoryImpl


class SurveyQuestionRepositoryTest(TestCase):

    @patch('survey.entity.survey_question.SurveyQuestion.save')
    def test_create_survey_question_success(self, mock_save):
        real_survey = Survey(id=1, title="Test Survey", description="A test survey")

        survey_question_repository = SurveyQuestionRepositoryImpl()
        result = survey_question_repository.create(real_survey, "What is your opinion on AI?", SurveyType.GENERAL)

        self.assertIsInstance(result, SurveyQuestion)
        self.assertEqual(result.survey, real_survey)
        self.assertEqual(result.question_text, "What is your opinion on AI?")
        self.assertEqual(result.survey_type, SurveyType.GENERAL)

        mock_save.assert_called_once()

    @patch('survey.repository.survey_question_repository_impl.SurveyQuestionRepositoryImpl')
    def test_create_survey_question_failure(self, MockSurveyQuestionRepositoryImpl):
        mock_repository = MockSurveyQuestionRepositoryImpl.return_value
        mock_repository.create.side_effect = ValueError("Survey must be an instance of Survey")
        survey_question_repository = SurveyQuestionRepositoryImpl()

        with self.assertRaises(ValueError) as context:
            survey_question_repository.create(None, "What is your opinion on AI?", SurveyType.GENERAL)

        self.assertEqual(str(context.exception), "Survey must be an instance of Survey")
