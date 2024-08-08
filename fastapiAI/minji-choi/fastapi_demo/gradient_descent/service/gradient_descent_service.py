from abc import ABC, abstractmethod
class GradientDescentService(ABC):
    @abstractmethod
    def gradientDescentTrain(self):
        pass
    @abstractmethod
    def saveTrainedModel(self, trainedModel, path):
        pass

    @abstractmethod
    def gradientDescentPredict(self, requestForm):
        pass
    @abstractmethod
    def checkValidation(self):
        pass