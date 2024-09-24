from backlog_status.entity.backlog_status_type import BacklogStatusType
from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl
from backlog_status.repository.backlog_status_repository_impl import BacklogStatusRepositoryImpl
from backlog_status.service.backlog_status_service import BacklogStatusService


class BacklogStatusServiceImpl(BacklogStatusService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__backlogStatusRepository = BacklogStatusRepositoryImpl.getInstance()
            cls.__instance.__backlogRepository = BacklogRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createBacklogStatus(self, backlogId, status):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogStatusRepository.create(backlog, BacklogStatusType.BACKLOG)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e

    def modifyBacklogStatus(self, backlogId, status):
        if not isinstance(status, str):
            raise ValueError("Status must be a string")

        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogStatusRepository.modify(backlog, status)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e
