from abc import ABC, abstractmethod


class PrincipalComponentAnalysisService(ABC):
    @abstractmethod
    def pcaAnalysis(self):
        pass
