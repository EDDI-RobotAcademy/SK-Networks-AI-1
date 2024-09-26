from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl
from backlog_issue.repository.backlog_domain_repository_impl import BacklogIssueRepositoryImpl
from backlog_issue.service.backlog_issue_service import BacklogIssueService


class BacklogIssueServiceImpl(BacklogIssueService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__backlogRepository = BacklogRepositoryImpl.getInstance()
            cls.__instance.__backlogIssueRepository = BacklogIssueRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createBacklogIssue(self, backlogId, issue):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogIssueRepository.create(backlog, issue)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e

    def modifyBacklogIssue(self, backlogId, issue):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogIssueRepository.modify(backlog, issue)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e
