from abc import ABC, abstractmethod


class DecisionTreeService(ABC):
    @abstractmethod
    def decisionTreeTrain(self):
        pass
    