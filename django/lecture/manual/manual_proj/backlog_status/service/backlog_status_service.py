from abc import ABC, abstractmethod


class BacklogStatusService(ABC):
    @abstractmethod
    def createBacklogStatus(self, backlogId, status):
        pass

    @abstractmethod
    def modifyBacklogStatus(self, backlogId, status):
        pass
    