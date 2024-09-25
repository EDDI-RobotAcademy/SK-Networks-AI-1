from abc import ABC, abstractmethod


class BacklogService(ABC):
    @abstractmethod
    def createBacklog(self, title):
        pass
    