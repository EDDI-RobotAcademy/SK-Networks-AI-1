from abc import ABC, abstractmethod


class BacklogTodoRepository(ABC):
    @abstractmethod
    def create(self, backlog, todo):
        pass

    @abstractmethod
    def modify(self, backlog, todo):
        pass
