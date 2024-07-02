from abc import ABC, abstractmethod


class DecisionTreeServcie(ABC):
    @abstractmethod
    def decisionTreeTrain(self):
        pass