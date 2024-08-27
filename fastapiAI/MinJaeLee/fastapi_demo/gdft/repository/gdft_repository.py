from abc import ABC, abstractmethod


class GDFTRepository(ABC):
    @abstractmethod
    def acquireTokenFromPretrainedModel(self):
        pass

    @abstractmethod
    def acquireModelFromPretrainedModel(self):
        pass

    @abstractmethod
    def loadDataset(self, tokenizer):
        pass

    @abstractmethod
    def configTrainingParameter(self):
        pass

    @abstractmethod
    def configTrainer(self, model, trainingParameter, needToTrainDataset, tokenizer):
        pass

    @abstractmethod
    def trainFineTuning(self, trainer):
        pass
