from abc import ABC, abstractmethod


class GradientDescentRepository(ABC):
    @abstractmethod
    def createTrainData(self):
        pass
    