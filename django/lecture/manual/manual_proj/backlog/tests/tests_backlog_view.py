from unittest import TestCase
from unittest.mock import patch, MagicMock

from django.core.exceptions import ObjectDoesNotExist

from backlog.entity.backlog import Backlog
from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl
from backlog.service.backlog_service_impl import BacklogServiceImpl

class BacklogServiceTest(TestCase):

    @patch('backlog.service.backlog_service_impl.BacklogRepositoryImpl')
    def test_create_backlog_success(self, MockBacklogRepositoryImpl):
        mockBacklog = MagicMock(spec=Backlog)
        mockBacklog.title = "Test Backlog"

        mockRepository = MockBacklogRepositoryImpl.getInstance.return_value
        mockRepository.create.return_value = mockBacklog

        BacklogServiceImpl._BacklogServiceImpl__instance = None
        backlogService = BacklogServiceImpl.getInstance()

        result = backlogService.createBacklog("Test Backlog")

        self.assertEqual(result, mockBacklog)
        mockRepository.create.assert_called_once_with("Test Backlog")

    @patch('backlog.service.backlog_service_impl.BacklogRepositoryImpl')
    def test_create_backlog_failure(self, MockBacklogRepositoryImpl):
        mockRepository = MockBacklogRepositoryImpl.getInstance.return_value
        mockRepository.create.return_value = None

        BacklogServiceImpl._BacklogServiceImpl__instance = None
        backlogService = BacklogServiceImpl.getInstance()

        result = backlogService.createBacklog("Test Backlog")

        self.assertIsNone(result)
        mockRepository.create.assert_called_once_with("Test Backlog")

    @patch('backlog.repository.backlog_repository_impl.Backlog')
    def test_findById_success(self, MockBacklog):
        mock_backlog_instance = MagicMock(spec=Backlog)
        mock_backlog_instance.id = 1
        mock_backlog_instance.title = "Test Backlog"

        MockBacklog.objects.get.return_value = mock_backlog_instance

        repository = BacklogRepositoryImpl.getInstance()
        found_backlog = repository.findById(1)

        self.assertEqual(found_backlog.id, mock_backlog_instance.id)
        self.assertEqual(found_backlog.title, mock_backlog_instance.title)
        MockBacklog.objects.get.assert_called_once_with(id=1)

    @patch('backlog.repository.backlog_repository_impl.Backlog')
    def test_findById_notFound(self, MockBacklog):
        MockBacklog.objects.get.side_effect = ObjectDoesNotExist()

        repository = BacklogRepositoryImpl.getInstance()

        with self.assertRaises(ValueError) as context:
            repository.findById(9999)

        self.assertEqual(str(context.exception), "Backlog with id 9999 does not exist")
        MockBacklog.objects.get.assert_called_once_with(id=9999)
