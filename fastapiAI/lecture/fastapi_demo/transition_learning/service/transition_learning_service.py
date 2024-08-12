from abc import ABC, abstractmethod


class TransitionLearningService(ABC):
    @abstractmethod
    def predictText(self, transitionLearningPredictRequestForm):
        pass

    @abstractmethod
    def transitionLearningWithsentimentAnalysis(self, sentimentAnalysisRequestForm):
        pass

    @abstractmethod
    def predictTextWithGPT2(self, gpt2PretrainedPredictionRequestForm):
        pass
