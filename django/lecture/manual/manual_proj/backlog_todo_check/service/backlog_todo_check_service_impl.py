
from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl
from backlog_todo_check.service.backlog_todo_check_service import BacklogTodoCheckService


class BacklogTodoCheckServiceImpl(BacklogTodoCheckService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__backlogRepository = BacklogRepositoryImpl.getInstance()
            cls.__instance.__backlogTodoCheckRepository = BacklogTodoCheckRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createBacklogTodoCheck(self, backlogId, isChecked):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogTodoCheckRepository.create(backlog, isChecked)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e

    def modifyBacklogTodoCheck(self, backlogId, isChecked):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogTodoCheckRepository.modify(backlog, isChecked)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e
