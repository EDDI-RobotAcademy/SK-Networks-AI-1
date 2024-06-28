import os

import joblib
import numpy as np
import pandas as pd
import tensorflow as tf

from orders_analysis.repository.orders_analysis_repository_impl import OrdersAnalysisRepositoryImpl
from orders_analysis.service.orders_analysis_service import OrdersAnalysisService


class OrdersAnalysisServiceImpl(OrdersAnalysisService):

    def __init__(self):
        self.__ordersAnalysisRepository = OrdersAnalysisRepositoryImpl()

    async def readExcel(self):
        currentDirectory = os.getcwd()
        print(f"currentDirectory: {currentDirectory}")

        filePath = os.path.join(
            currentDirectory, "..", "assets", "orders_data_after_drop_duplication.xlsx"
        )

        try:
            dataFrame = pd.read_excel(filePath)
            return dataFrame
        except FileNotFoundError:
            print(f"파일이 존재하지 않습니다: {filePath}")

    async def trainModel(self):
        dataFrame = await self.readExcel()
        X_scaled, y, scaler = \
            await self.__ordersAnalysisRepository.prepareViewCountVsQuantity(dataFrame)

        joblib.dump(scaler, "ordersModelScaler.pkl")

        X_train, X_test, y_train, y_test = \
            await self.__ordersAnalysisRepository.splitTrainTestData(X_scaled, y)
        print(f"X_train: {X_train}, y_train: {y_train},"
              f"X_test: {X_test}, y_test: {y_test}")

        numberOfModels = 10
        modelList = []

        for index in range(numberOfModels):
            print(f"Training model {index + 1} / {numberOfModels}")

            model = await self.__ordersAnalysisRepository.createModel()
            print("is it pass createModel()")
            await self.__ordersAnalysisRepository.fitModel(model, X_train, y_train)
            print("is it pass fitModel()")
            model.save(f"ordersModel_{index + 1}.h5")
            modelList.append(model)

        return f"Trained {numberOfModels} models 성공~~!!~!"

    def predictQuantityFromModel(self, viewCount):
        print(f"predictQuantityFromModel -> viewCount: {viewCount}")

        scaler = joblib.load('ordersModelScaler.pkl')
        print(f"after load scaler")

        ordersPredictionList = []

        for index in range(1, 11):
            print(f"ordersModel_{index}.h5")
            ordersModelFileName = f"ordersModel_{index}.h5"
            ordersModel = tf.keras.models.load_model(f"./{ordersModelFileName}", compile=True)
            print(f"after load model")
            X_pred = np.array([[viewCount]])
            X_pred_scaled = self.__ordersAnalysisRepository.transformFromScaler(scaler, X_pred)

            ordersPredict = self.__ordersAnalysisRepository.predictFromModel(
                ordersModel, X_pred_scaled)

            ordersPredictionList.append(float(ordersPredict))

        averagePrediction = np.mean(ordersPredictionList)
        print(f"averagePrediction: {averagePrediction}")

        return averagePrediction
