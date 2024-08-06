from abc import ABC, abstractmethod


class SequenceAnalysisRepository(ABC):
    @abstractmethod
    def createTokenizer(self, userSendMessage):
        pass

    @abstractmethod
    def extractSequence(self, tokenizer, userSendMessage):
        pass
