from abc import ABC, abstractmethod


class RandomForestService(ABC):
    @abstractmethod
    def randomForestAnalysis(self):
        pass

