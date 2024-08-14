from abc import ABC, abstractmethod


class SequenceAnalysisService(ABC):
    @abstractmethod
    def predictNextSequence(self, userSendMessage):
        pass