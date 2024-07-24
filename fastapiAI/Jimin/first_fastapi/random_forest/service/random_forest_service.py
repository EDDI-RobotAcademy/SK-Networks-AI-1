from abc import ABC, abstractmethod

class RandomForestService(ABC):
    @abstractmethod
    def readCsv(self):
        pass

    @abstractmethod
    def featureTargetVariableDefinition(self, dataEncoded):
        pass

    @abstractmethod
    def randomForestAnalysis(self):
        pass