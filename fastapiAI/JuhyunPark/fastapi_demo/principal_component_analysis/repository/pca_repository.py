from abc import ABC, abstractmethod


class PrincipalComponentAnalysisRepository(ABC):
    @abstractmethod
    def createPCASample(self):
        pass

    @abstractmethod
    def configCovariance(self, numberOfFeatures):
        pass

    @abstractmethod
    def configZeroMean(self, numberOfFeatures):
        pass

    @abstractmethod
    def createMultiVariateNormalDistribution(self, mean, covariance, numberOfPoints):
        pass

    @abstractmethod
    def createDataFrame(self, createdMultiVariateData, numberOfFeatures):
        pass

    @abstractmethod
    def readyForAnalysis(self, numberOfComponents):
        pass

    @abstractmethod
    def fitTransform(self, pca, createdDataFrame):
        pass