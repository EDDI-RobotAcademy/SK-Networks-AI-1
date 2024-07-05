from abc import ABC, abstractmethod


class ConvolutionNeuralNetworkRepository(ABC):
    @abstractmethod
    def loadCifar10Data(self):
        pass

    @abstractmethod
    def filteringClasses(self, imageList, labelList, targetClassList):
        pass

    @abstractmethod
    def createDataGenerator(self, trainImageList, trainLabelList, testImageList, testLabelList):
        pass