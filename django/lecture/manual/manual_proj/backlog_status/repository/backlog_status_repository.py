from abc import ABC, abstractmethod


class BacklogStatusRepository(ABC):
    @abstractmethod
    def create(self, backlog, status):
        pass

    @abstractmethod
    def modify(self, backlog, status):
        pass
