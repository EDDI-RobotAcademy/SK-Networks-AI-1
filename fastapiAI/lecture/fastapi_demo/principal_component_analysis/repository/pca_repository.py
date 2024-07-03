from abc import ABC, abstractmethod


class PrincipalComponentAnalysisRepository(ABC):
    @abstractmethod
    def createPCASample(self):
        pass
