import os
import pandas as pd
from random_forest.service.random_forest_service import RandomForestService
from random_forest.repository.random_forest_repository_impl import RandomForestRepositoryImpl
from random_forest.controller.response_form.random_forest_response_form import RandomForestResponseForm


class RandomForestServiceImpl(RandomForestService):
    def __init__(self):
        self.__randomForestRepository = RandomForestRepositoryImpl()

    def readCsv(self):
        currentDirectory = os.getcwd()
        filePath = os.path.join(currentDirectory, 'assets', 'customer_booking.csv')
        # print('filepath: ', filePath)
        dataFrame = pd.read_csv(filePath, encoding='latin1')
        return dataFrame

    # 피처 타겟 변수 정의. 실제로 레포지토리에서 할 작업이 아니긴 함
    def featureTargetVariableDefinition(self, dataEncoded):
        # print('featureTargetVariableDefinition()')
        X = dataEncoded.drop('booking_complete', axis=1)
        y = dataEncoded['booking_complete']
        return X,y

    def randomForestAnalysis(self):

        dataFrame = self.readCsv()
        dataEncoded, labelEncoders = (self.__randomForestRepository.flightCategoricalVariableEncoding(dataFrame))
        X,y = self.featureTargetVariableDefinition(dataEncoded)
        # print('X: ', X)
        # print('y: ', y)

        X_train, X_test, y_train, y_test = (self.__randomForestRepository.splitTrainTestSet(X,y))

        randomForestmodel = self.__randomForestRepository.train(X_train, y_train)
        y_pred = self.__randomForestRepository.predict(randomForestmodel, X_test)

        accuracy, report, confusionMatrix = self.__randomForestRepository.evaluate(y_test, y_pred)

        X_resampled, y_resampled = self.__randomForestRepository.applysmote(X_train, y_train)
        randomForestModelAfterSmote = self.__randomForestRepository.train(X_resampled, y_resampled)
        y_pred_after_smote = self.__randomForestRepository.predict(randomForestModelAfterSmote, X_test)

        smoteAccuracy, smoteReport, smoteConfusionMatrix = self.__randomForestRepository.evaluate(y_test, y_pred_after_smote)

        return RandomForestResponseForm.createForm(
            confusionMatrix, smoteConfusionMatrix,
            y_test, y_pred, y_pred_after_smote, dataFrame)

        # self.__randomForestRepository.evaluate()


