from abc import ABC,abstractmethod

class SentenceStructureAnalysisService(ABC):

    @abstractmethod
    def sentenceTokenize(self, sentenceRequest):
        pass

    @abstractmethod
    def wordTokenize(self, sentenceRequest):
        pass

    @abstractmethod
    def sentenceAnalysis(self, sentenceRequest):
        pass