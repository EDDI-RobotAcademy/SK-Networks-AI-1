from abc import ABC, abstractmethod


class BacklogTodoCheckRepository(ABC):
    @abstractmethod
    def create(self, backlog, isChecked):
        pass

    @abstractmethod
    def modify(self, backlog, isChecked):
        pass
