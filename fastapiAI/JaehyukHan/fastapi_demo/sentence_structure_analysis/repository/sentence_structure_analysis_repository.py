from abc import ABC, abstractmethod


class SentenceStructureAnalysisRepository(ABC):
    @abstractmethod
    def sentenceTokenize(self, sentenceRequest):
        pass

    @abstractmethod
    def wordTokenize(self, text):
        pass

    @abstractmethod
    def sentenceAnalysis(self, text):
        pass