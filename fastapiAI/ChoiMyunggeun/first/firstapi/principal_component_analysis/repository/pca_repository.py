from abc import ABC, abstractmethod


class PrincipalComponentAnalysisRepository(ABC):
    @abstractmethod
    def createPCASample(self):
        ...

    @abstractmethod
    def configCovariance(self, numberOfFeatures):
        ...

    @abstractmethod
    def configZeroMean(self, numberOfFeatures):
        ...


    @abstractmethod
    def createMultiVariateNormalDistribution(self, mean, convaraianve, numberOfPoints):
        ...

    @abstractmethod
    def readyForAnalysis(self, numberOfComponents):
        ...

    @abstractmethod
    def fitTransform(self, pca, createdDataFrame):
        ...
