from abc import abstractmethod, ABC


class PrincipalComponentAnalysisService(ABC):
    @abstractmethod
    def pcaAnalysis(self):
        pass