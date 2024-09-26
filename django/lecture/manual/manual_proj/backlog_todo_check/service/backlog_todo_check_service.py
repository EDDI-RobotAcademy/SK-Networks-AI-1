from abc import ABC, abstractmethod


class BacklogTodoCheckService(ABC):
    @abstractmethod
    def createBacklogTodoCheck(self, backlogId, isChecked):
        pass

    @abstractmethod
    def modifyBacklogTodoCheck(self, backlogId, isChecked):
        pass
