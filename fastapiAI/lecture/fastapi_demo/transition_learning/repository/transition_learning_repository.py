from abc import abstractmethod, ABC


class TransitionLearningRepository(ABC):
    @abstractmethod
    def prepareBertBaseUncasedLearningSet(self):
        pass

    @abstractmethod
    def prepareBertBaseMultilingualUncasedSentimentLearningSet(self):
        pass
