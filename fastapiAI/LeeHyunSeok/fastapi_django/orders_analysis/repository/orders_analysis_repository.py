from abc import ABC, abstractmethod


class OrdersAnalysisRepository(ABC):

    @abstractmethod
    def prepareViewCountVsQuantity(self, dataFrame):
        pass

    @abstractmethod
    def splitTrainTestData(self, X_scaled, y):
        pass

    @abstractmethod
    def createModel(self):
        pass

    @abstractmethod
    def fitModel(self, model, X_train, y_train):
        pass

    @abstractmethod
    def transformFromScaler(self, scaler, X_pred):
        pass

    @abstractmethod
    def predictFromModel(self, ordersModel, X_pred_scaled):
        pass