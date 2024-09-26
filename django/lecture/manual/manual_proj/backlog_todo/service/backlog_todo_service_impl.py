
from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl
from backlog_todo.repository.backlog_todo_repository_impl import BacklogTodoRepositoryImpl
from backlog_todo.service.backlog_todo_service import BacklogTodoService


class BacklogTodoServiceImpl(BacklogTodoService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__backlogRepository = BacklogRepositoryImpl.getInstance()
            cls.__instance.__backlogTodoRepository = BacklogTodoRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createBacklogTodo(self, backlogId, todo):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogTodoRepository.create(backlog, todo)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e

    def modifyBacklogTodo(self, backlogId, todo):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogTodoRepository.modify(backlog, todo)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e
