from abc import ABC, abstractmethod


class BacklogSuccessCriteriaRepository(ABC):
    @abstractmethod
    def create(self, backlog, successCriteria):
        pass

    @abstractmethod
    def modify(self, backlog, successCriteria):
        pass
