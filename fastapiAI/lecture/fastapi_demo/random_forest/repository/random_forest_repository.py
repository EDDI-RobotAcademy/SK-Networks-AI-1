from abc import ABC, abstractmethod


class RandomForestRepository(ABC):
    @abstractmethod
    def evaluate(self):
        pass
