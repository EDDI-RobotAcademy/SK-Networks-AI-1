from abc import ABC, abstractmethod

class DecisionTreeRepository(ABC):
    @abstractmethod
    def loadWineInfo(self):
        ...

    @abstractmethod
    def createDataFrame(self, data, feature_names):
        ...

    @abstractmethod
    def splitTrainTestSet(self, wineDataFeame):
        ...

    @abstractmethod
    def applyStandardScaler(self, trainDataFrame, testDataFrame, featureNames):
        ...

    @abstractmethod
    def sliceTensor(self, scaledTrainDataFrame, scaledTestDataFrame):
        ...

    @abstractmethod
    def applyBatchSize(self, trainDataFrameAfterSlice,testDataFrameAfterSlice, batchSize):
        ...

    @abstractmethod
    def learn(self, readyForLearnTrainData):
        ...
