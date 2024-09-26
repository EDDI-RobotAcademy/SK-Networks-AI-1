from abc import ABC, abstractmethod


class BacklogReviewService(ABC):
    @abstractmethod
    def createBacklogReview(self, backlogId, review):
        pass

    @abstractmethod
    def modifyBacklogReview(self, backlogId, review):
        pass
