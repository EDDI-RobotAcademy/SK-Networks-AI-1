from abc import ABC, abstractmethod


class SequenceAnalysisRepository(ABC):
    @abstractmethod
    def createTokenizer(self, userSendMessage):
        pass

    @abstractmethod
    def extractSequence(self, tokenizer, userSendMessage):
        pass

    @abstractmethod
    def paddingSequence(self, inputSequences, maxSequenceLength):
        pass

    @abstractmethod
    def separateInputAndOutputSequences(self, paddedInputSequences, totalWords):
        pass

    @abstractmethod
    def trainSequence(self, totalWords, maxSequenceLength, X, y):
        pass

    @abstractmethod
    def generateText(self, firstText, wannaCreateTextNumber, trainedModel, maxSequenceLength, tokenizer):
        pass