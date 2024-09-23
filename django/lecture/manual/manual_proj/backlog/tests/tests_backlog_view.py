from unittest import TestCase
from unittest.mock import patch, MagicMock

from backlog.entity.backlog import Backlog
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
