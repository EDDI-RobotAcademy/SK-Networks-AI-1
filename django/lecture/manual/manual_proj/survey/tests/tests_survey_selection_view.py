from unittest import TestCase
from unittest.mock import patch, MagicMock
from survey.repository.survey_selection_repository_impl import SurveySelectionRepositoryImpl
from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_selection import SurveySelection

class SurveySelectionRepositoryTest(TestCase):

    @patch('survey.repository.survey_selection_repository_impl.SurveySelection')
    @patch('survey.entity.survey_question.SurveyQuestion')
    def test_create_survey_selection_failure(self, MockSurveyQuestion, MockSurveySelection):
        mock_repository = MagicMock(spec=SurveySelectionRepositoryImpl)
        mock_repository.createSurveySelection.side_effect = ValueError("Invalid question")

        # Create a mock instance of SurveyQuestion with necessary attributes
        mock_question = MagicMock(spec=SurveyQuestion)
        mock_question._state = MagicMock()

        # Mock SurveySelection's save method
        mock_selection = MockSurveySelection.return_value
        mock_selection.save.side_effect = ValueError("Invalid question")

        survey_selection_repository = SurveySelectionRepositoryImpl.getInstance()

        # Ensure the exception is properly raised
        with self.assertRaises(ValueError):
            survey_selection_repository.createSurveySelection(mock_question, "Selection Text")

    @patch('survey.repository.survey_selection_repository_impl.SurveySelection')
    @patch('survey.entity.survey_question.SurveyQuestion')
    def test_create_survey_selection_success(self, MockSurveyQuestion, MockSurveySelection):
        mock_question = MagicMock(spec=SurveyQuestion)
        mock_question._state = MagicMock()

        mock_selection = MagicMock(spec=SurveySelection)
        MockSurveySelection.return_value = mock_selection
        mock_selection.save.return_value = None

        survey_selection_repository = SurveySelectionRepositoryImpl.getInstance()
        result = survey_selection_repository.createSurveySelection(mock_question, "Selection Text")

        mock_selection.save.assert_called_once()
        self.assertIs(result, mock_selection)

        mock_selection.selection_text = "Selection Text"
        self.assertEqual(mock_selection.selection_text, "Selection Text")

        MockSurveySelection.assert_called_once_with(question=mock_question, selection_text="Selection Text")
