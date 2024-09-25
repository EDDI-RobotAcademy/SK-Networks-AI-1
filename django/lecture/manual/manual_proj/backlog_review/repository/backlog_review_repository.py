from abc import ABC, abstractmethod


class BacklogReviewRepository(ABC):
    @abstractmethod
    def create(self, backlog, review):
        pass

    @abstractmethod
    def modify(self, backlog, review):
        pass
