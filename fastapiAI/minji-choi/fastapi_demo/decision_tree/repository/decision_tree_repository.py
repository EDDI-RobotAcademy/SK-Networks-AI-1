from abc import ABC,  abstractmethod

class DecisionTreeRepository(ABC):
    @abstractmethod
    def loadWineInfo (self):
        pass

    @abstractmethod
    def createDataFrame(self, data, featureNames):
        pass
    @abstractmethod
    def splitTrainTestSet(self, dataframe):
        pass
    @abstractmethod
    def applyStandardScaler(self, trainDataFrame, testDataFrame, featureNames):
        pass

    @abstractmethod
    def sliceTensor(self, trainDataFrame, testDataFrame):
        pass

    @abstractmethod
    def applyBatchSize(self, trainTensor, testTensor, batchSize):
        pass

    @abstractmethod
    def learn(self, trainTensor):
        pass
