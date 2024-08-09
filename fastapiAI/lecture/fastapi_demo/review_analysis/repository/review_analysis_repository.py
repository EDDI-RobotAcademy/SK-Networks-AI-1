from abc import ABC, abstractmethod


class ReviewAnalysisRepository(ABC):
    @abstractmethod
    def reviewTrain(self):
        pass

    @abstractmethod
    def preprocess(self, xData, yData, englishStop):
        pass

    @abstractmethod
    def splitTrainTestSet(self, xMeanfulData, yData):
        pass

    @abstractmethod
    def tokenize(self, xTrain, xTest, reviewMaxLength):
        pass
