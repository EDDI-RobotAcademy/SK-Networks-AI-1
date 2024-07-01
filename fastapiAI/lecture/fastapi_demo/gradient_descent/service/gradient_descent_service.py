from abc import ABC, abstractmethod


class GradientDescentService(ABC):
    @abstractmethod
    def gradientDescentTrain(self):
        pass
