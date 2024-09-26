from abc import ABC, abstractmethod


class BacklogDomainService(ABC):
    @abstractmethod
    def createBacklogDomain(self, backlogId, domain):
        pass

    @abstractmethod
    def modifyBacklogDomain(self, backlogId, domain):
        pass
