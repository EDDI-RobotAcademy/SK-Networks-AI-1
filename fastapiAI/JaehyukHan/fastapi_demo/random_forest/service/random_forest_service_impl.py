from random_forest.controller.reponse_form.random_forest_response_form import RandomForestResponseForm
from random_forest.repository.random_forest_repository_impl import RandomForestRepositoryImpl
from random_forest.service.random_forest_service import RandomForestService

import os
import pandas as pd


class RandomForestServiceImpl(RandomForestService):
    def __init__(self):
        self.__randomForestRepository = RandomForestRepositoryImpl()

    def readCsv(self):
        currentDirectory = os.getcwd()

        filePath = os.path.join(currentDirectory, '..', 'assets', 'customer_booking.csv')

        dataFrame = pd.read_csv(filePath, encoding='latin1')

        return dataFrame

    # 특정 타겟 변수를 정의
    def featureTargetVariableDefinition(self, dataEncoded):
        print('featureTargetVariableDefinition()')

        X = dataEncoded.drop('booking_complete', axis=1)
        y = dataEncoded['booking_complete']

        return X, y

    def randomForestAnalysis(self):
        print('randomForestAnalysis()')

        dataFrame = self.readCsv()
        dataEncoded, labelEncoders = (self.__randomForestRepository.flightCategoricalVariableEncoding(dataFrame))

        X, y = self.featureTargetVariableDefinition(dataEncoded)
        # print(f"X: {X}")
        # print(f"y: {y}")

        X_train, X_test, y_train, y_test = (self.__randomForestRepository.splitTrainTestSet(X, y))
        randomForestModel = self.__randomForestRepository.train(X_train, y_train)

        y_pred = self.__randomForestRepository.predict(randomForestModel, X_test)

        accuracy, report, confusionMatrix = (self.__randomForestRepository.evaluate(y_test, y_pred))

        X_resampled, y_resampled = self.__randomForestRepository.applySmote(X_train, y_train)
        randomForestModelAfterSmote = self.__randomForestRepository.train(X_resampled, y_resampled)
        y_pred_after_smote = (self.__randomForestRepository.predict(randomForestModelAfterSmote, X_test))
        smoteAccuracy, smoteReport, smoteConfustionMatrix = (self.__randomForestRepository.evaluate(y_test, y_pred_after_smote))

        return RandomForestResponseForm.createForm(
            confusionMatrix, smoteConfustionMatrix,
            y_test, y_pred, y_pred_after_smote, dataFrame
        )