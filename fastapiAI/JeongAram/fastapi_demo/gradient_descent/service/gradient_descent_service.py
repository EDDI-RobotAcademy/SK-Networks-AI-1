from abc import ABC, abstractmethod

class GradientDescentService(ABC):
    @abstractmethod
    def gradientDescentTrain(self):
        pass

    @abstractmethod
    def checkValidation(self):
        pass

    @abstractmethod
    def gradientDescentPredict(self, request):
        pass
