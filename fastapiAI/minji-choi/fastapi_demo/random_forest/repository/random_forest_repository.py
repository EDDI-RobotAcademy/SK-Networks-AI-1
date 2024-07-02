from abc import ABC, abstractmethod


class RandomForestRepository(ABC):
    @abstractmethod
    def evaluate(self, y_test, y_pred):
        pass

    @abstractmethod
    def flightCategoricalVariableEncoding(self, dataFrame):
        pass

    @abstractmethod
    def splitTrainTestSet(self,X,y):
        pass

    def train(self, X_train, y_train):
        pass

    def predict(self, randomForestModel, X_test):
        pass

    def applysmote(self, X_train, y_train):
        pass