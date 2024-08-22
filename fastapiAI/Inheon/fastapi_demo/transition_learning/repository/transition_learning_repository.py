from abc import ABC, abstractmethod


class TransitionLearningRepository(ABC):
    @abstractmethod
    def prepareLearningSet(self):
        pass