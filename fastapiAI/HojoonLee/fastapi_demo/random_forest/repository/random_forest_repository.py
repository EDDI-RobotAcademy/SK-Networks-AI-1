from abc import ABC, abstractmethod


class RandomForestRepository(ABC):
    @abstractmethod
    def flightCategoricalVariableEncoding(self, dataFrame):
        pass

    @abstractmethod
    def splitTrainTest(self, X, y):
        pass

    @abstractmethod
    def train(self, X_train, y_train):
        pass

    @abstractmethod
    def predict(self, randomForestModel, X_test):
        pass

    @abstractmethod
    def evaluate(self, y_pred, y_test):
        pass

    @abstractmethod
    def applySmote(self, X_train, y_train):
        pass