from abc import ABC, abstractmethod

class RandomForestService(ABC):
    @abstractmethod
    def randomForestAnalysis(self):
        pass
    @abstractmethod
    def featureTargetVariableDefinition(self, dataEncoded):
        pass