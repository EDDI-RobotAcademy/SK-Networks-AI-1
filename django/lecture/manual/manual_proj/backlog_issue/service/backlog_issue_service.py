from abc import ABC, abstractmethod


class BacklogIssueService(ABC):
    @abstractmethod
    def createBacklogIssue(self, backlogId, issue):
        pass

    @abstractmethod
    def modifyBacklogIssue(self, backlogId, issue):
        pass
