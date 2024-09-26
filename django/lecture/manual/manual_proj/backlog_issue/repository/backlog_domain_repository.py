from abc import ABC, abstractmethod


class BacklogIssueRepository(ABC):
    @abstractmethod
    def create(self, backlog, issue):
        pass

    @abstractmethod
    def modify(self, backlog, issue):
        pass
