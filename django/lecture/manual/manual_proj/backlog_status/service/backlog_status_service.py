from abc import ABC, abstractmethod


class BacklogStatusService(ABC):
    @abstractmethod
    def modifyBacklogStatus(self, backlogId, status):
        pass
    