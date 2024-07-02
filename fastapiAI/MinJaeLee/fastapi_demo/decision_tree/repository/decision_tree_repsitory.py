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
    def applyStandardScaler(self, trainDataFrame, testDataFrame, featureNames):
        pass

    @abstractmethod
    def sliceTensor(self, scaledTraindedDataFrame, scaledTestDataFrame):
        pass

    @abstractmethod
    def applyBatchSize(self, trainDataFrameAfterSlice, testDataFrameAfterSlice, batch_size):
        pass

    @abstractmethod
    def learn(self, readyForLearnTrainData):
        pass