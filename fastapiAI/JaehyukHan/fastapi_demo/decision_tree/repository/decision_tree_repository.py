from abc import ABC, abstractmethod


class DecisionTreeRepository(ABC):
    @abstractmethod
    def loadWineInfo(self):
        pass

    @abstractmethod
    def createDataFrame(self, data, featureNames):
        pass

    @abstractmethod
    def splitTrainTestSet(self, wineDataFrame):
        pass

    @abstractmethod
    def applyStandardScaler(self, trainDataFrame, testDataFrame, featureName):
        pass

    @abstractmethod
    def sliceTensor(self, scaledTrainDataFrame, scaledTestDataFrame):
        pass

    @abstractmethod
    def applyBatchSize(self, trainDataFrameAfterSlice, testDataFrameAfterSlice, batchsize):
        pass

    @abstractmethod
    def learn(self, readyForLearnTrainData):
        pass