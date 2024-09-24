from abc import ABC, abstractmethod


class BacklogDomainRepository(ABC):
    @abstractmethod
    def create(self, domain):
        pass

    @abstractmethod
    def findById(self, backlogDomainId):
        pass
