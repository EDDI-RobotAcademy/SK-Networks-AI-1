from abc import ABC, abstractmethod

class DecisionTreeRepository(ABC):
    @abstractmethod
    def loadWineInfo(self):
        ...
