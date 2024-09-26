from backlog_status.entity.backlog_status_type import BacklogStatusType
from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl
from backlog_success_criteria.repository.backlog_success_criteria_repository_impl import \
    BacklogSuccessCriteriaRepositoryImpl
from backlog_success_criteria.service.backlog_success_criteria_service import BacklogSuccessCriteriaService


class BacklogSuccessCriteriaServiceImpl(BacklogSuccessCriteriaService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__backlogSuccessCriteriaRepository = BacklogSuccessCriteriaRepositoryImpl.getInstance()
            cls.__instance.__backlogRepository = BacklogRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createBacklogSuccessCriteria(self, backlogId, successCriteria):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogSuccessCriteriaRepository.create(backlog, successCriteria)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e

    def modifyBacklogSuccessCriteria(self, backlogId, successCriteria):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogSuccessCriteriaRepository.modify(backlog, successCriteria)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e
