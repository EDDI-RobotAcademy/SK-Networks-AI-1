from abc import ABC, abstractmethod


class ReviewAnalysisService(ABC):
    @abstractmethod
    def reviewAnalysis(self):
        pass

    @abstractmethod
    def sentimentAnalysis(self, userReviewRequestForm):
        pass
