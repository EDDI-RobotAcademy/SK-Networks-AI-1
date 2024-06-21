import os

from random_forest.repository.random_forest_repository_impl import RandomForestRepositoryImpl
from random_forest.service.random_forest_service import RandomForestService

import pandas as pd


class RandomForestServiceImpl(RandomForestService):
    def __init__(self):
        self.__randomForestRepository = RandomForestRepositoryImpl()

    def readCsv(self):
        currentDirectory = os.getcwd()
        # print(f"currentDirectory: {currentDirectory}")

        filePath = os.path.join(currentDirectory, '..', 'assets', 'customer_booking.csv')
        # print(f"filePath: {filePath}")

        dataFrame = pd.read_csv(filePath, encoding='latin1')
        # print(f"dataFrame: {dataFrame}")
        return dataFrame

    # 특징 타겟 변수를 정의
    def featureTargetVariableDefinition(self, dataEncoded):
        print("featureTargetVariableDefinition()")

        X = dataEncoded.drop('booking_complete', axis=1)
        y = dataEncoded['booking_complete']

        return X, y

    def randomForestAnalysis(self):
        print("randomForestAnalysis()")

        dataFrame = self.readCsv()
        dataEncoded, labelEncoders = (
            self.__randomForestRepository.flightCategoricalVariableEncoding(dataFrame))

        X, y = self.featureTargetVariableDefinition(dataEncoded)
        # print(f"X: {X}")
        # print(f"y: {y}")

        self.__randomForestRepository.evaluate()

