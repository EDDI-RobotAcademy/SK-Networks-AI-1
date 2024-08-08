from abc import ABC, abstractmethod


class SentenceStructureAnalysisService(ABC):
    # 시나리오: 문장들을 던지고 문장들을 구별하게 하는 것.

    @abstractmethod
    def sentenceTokenize(self, sentenceRequest):
        pass

    @abstractmethod
    def wordTokenize(self, sentenceRequest):
        pass

    @abstractmethod
    def sentenceAnalysis(self, sentenceRequest):
        pass
