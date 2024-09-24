from unittest import TestCase
from unittest.mock import patch, MagicMock
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from backlog.entity.backlog_status import BacklogStatus
from backlog.repository.backlog_status_repository_impl import BacklogStatusRepositoryImpl

class BacklogStatusRepositoryImplTest(TestCase):

    @patch('backlog.entity.backlog_status.BacklogStatus.save')
    def test_create_backlog_status_success(self, mock_save):
        mock_save.return_value = None
        backlog_status_repo = BacklogStatusRepositoryImpl.getInstance()

        result = backlog_status_repo.create("OPEN")

        self.assertIsInstance(result, BacklogStatus)
        self.assertEqual(result.status, "OPEN")
        mock_save.assert_called_once()

    @patch('backlog.entity.backlog_status.BacklogStatus.save')
    def test_create_backlog_status_failure(self, mock_save):
        mock_save.side_effect = IntegrityError("Integrity error")
        backlog_status_repo = BacklogStatusRepositoryImpl.getInstance()

        result = backlog_status_repo.create("OPEN")

        self.assertIsNone(result)
        mock_save.assert_called_once()

    @patch('backlog.entity.backlog_status.BacklogStatus.objects.get')
    @patch('backlog.entity.backlog_status.BacklogStatus.save')
    def test_modify_backlog_status_success(self, mock_save, mock_get):
        mock_backlog = MagicMock()
        mock_backlog.id = 1
        mock_backlog_status = MagicMock()
        mock_backlog_status.status = "BACKLOG"
        mock_get.return_value = mock_backlog_status

        backlog_status_repo = BacklogStatusRepositoryImpl.getInstance()

        result = backlog_status_repo.modify(mock_backlog, "IN_PROGRESS")

        self.assertEqual(result.status, "IN_PROGRESS")
        mock_backlog_status.save.assert_called_once()
        mock_get.assert_called_once_with(backlog=mock_backlog)

    @patch('backlog.entity.backlog_status.BacklogStatus.objects.get')
    def test_modify_backlog_status_not_found(self, mock_get):
        mock_backlog = MagicMock()
        mock_backlog.id = 1
        mock_get.side_effect = ObjectDoesNotExist()  # Simulate not found

        backlog_status_repo = BacklogStatusRepositoryImpl.getInstance()

        with self.assertRaises(ValueError) as context:
            backlog_status_repo.modify(mock_backlog, "IN_PROGRESS")

        self.assertEqual(str(context.exception), "No backlog status found for backlog ID 1")
        mock_get.assert_called_once_with(backlog=mock_backlog)

    @patch('backlog.entity.backlog_status.BacklogStatus.objects.get')
    def test_modify_backlog_status_other_exception(self, mock_get):
        mock_backlog = MagicMock()
        mock_backlog.id = 1
        mock_get.side_effect = Exception("Some other error")  # Simulate other exceptions

        backlog_status_repo = BacklogStatusRepositoryImpl.getInstance()

        with self.assertRaises(Exception) as context:
            backlog_status_repo.modify(mock_backlog, "IN_PROGRESS")

        self.assertEqual(str(context.exception), "Some other error")
        mock_get.assert_called_once_with(backlog=mock_backlog)

