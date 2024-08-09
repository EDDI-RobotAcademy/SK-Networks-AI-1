from abc import ABC, abstractmethod


class SrbcbService(ABC):
    @abstractmethod
    def predict(self):
        pass
