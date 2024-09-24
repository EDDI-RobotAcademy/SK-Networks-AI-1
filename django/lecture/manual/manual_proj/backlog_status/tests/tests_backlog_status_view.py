from unittest import TestCase
from unittest.mock import patch, MagicMock
from django.core.exceptions import ObjectDoesNotExist

from backlog_status.entity.backlog_status_type import BacklogStatusType
from backlog_status.repository.backlog_status_repository_impl import BacklogStatusRepositoryImpl
from backlog_status.service.backlog_status_service_impl import BacklogStatusServiceImpl


class BacklogStatusRepositoryImplTest(TestCase):

    @patch('backlog.repository.backlog_repository_impl.BacklogRepositoryImpl.findById')
    @patch('backlog_status.repository.backlog_status_repository_impl.BacklogStatusRepositoryImpl.create')
    def test_create_backlog_status_success(self, mock_create, mock_find_by_id):
        mock_backlog = MagicMock()
        mock_find_by_id.return_value = mock_backlog

        mock_create.return_value = MagicMock()

        backlog_status_service = BacklogStatusServiceImpl.getInstance()

        result = backlog_status_service.createBacklogStatus(1)

        mock_find_by_id.assert_called_once_with(1)
        mock_create.assert_called_once_with(mock_backlog, BacklogStatusType.BACKLOG)

    @patch('backlog.repository.backlog_repository_impl.BacklogRepositoryImpl.findById')
    @patch('backlog_status.repository.backlog_status_repository_impl.BacklogStatusRepositoryImpl.create')
    def test_create_backlog_status_backlog_not_found(self, mock_create, mock_find_by_id):
        mock_find_by_id.return_value = None

        backlog_status_service = BacklogStatusServiceImpl.getInstance()

        with self.assertRaises(ValueError) as context:
            backlog_status_service.createBacklogStatus(1)

        self.assertEqual(str(context.exception), "Backlog with id 1 does not exist")
        mock_find_by_id.assert_called_once_with(1)
        mock_create.assert_not_called()

    @patch('backlog_status.entity.backlog_status.BacklogStatus.objects.get')
    @patch('backlog_status.entity.backlog_status.BacklogStatus.save')
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

    @patch('backlog_status.entity.backlog_status.BacklogStatus.objects.get')
    def test_modify_backlog_status_not_found(self, mock_get):
        mock_backlog = MagicMock()
        mock_backlog.id = 1
        mock_get.side_effect = ObjectDoesNotExist()

        backlog_status_repo = BacklogStatusRepositoryImpl.getInstance()

        with self.assertRaises(ValueError) as context:
            backlog_status_repo.modify(mock_backlog, "IN_PROGRESS")

        self.assertEqual(str(context.exception), "No backlog status found for backlog ID 1")
        mock_get.assert_called_once_with(backlog=mock_backlog)

    @patch('backlog_status.entity.backlog_status.BacklogStatus.objects.get')
    def test_modify_backlog_status_other_exception(self, mock_get):
        mock_backlog = MagicMock()
        mock_backlog.id = 1
        mock_get.side_effect = Exception("Some other error")

        backlog_status_repo = BacklogStatusRepositoryImpl.getInstance()

        with self.assertRaises(Exception) as context:
            backlog_status_repo.modify(mock_backlog, "IN_PROGRESS")

        self.assertEqual(str(context.exception), "Some other error")
        mock_get.assert_called_once_with(backlog=mock_backlog)

