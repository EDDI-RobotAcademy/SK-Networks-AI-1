from abc import ABC, abstractmethod


class BacklogStatusRepository(ABC):
    @abstractmethod
    def create(self, title):
        pass

    @abstractmethod
    def modify(self, backlog, status):
        pass
