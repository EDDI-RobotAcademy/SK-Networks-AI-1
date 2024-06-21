from abc import ABC, abstractmethod


class RandomForestRepository(ABC):
    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def flightCategoricalVariableEncoding(self, dataFrame):
        pass
