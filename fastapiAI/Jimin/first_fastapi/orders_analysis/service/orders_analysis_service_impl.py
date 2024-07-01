import os

import joblib
import pandas as pd
import tensorflow as tf
import numpy as np

from orders_analysis.repository.orders_analysis_repository_impl import OrdersAnalysisRepositoryImpl
from orders_analysis.service.orders_analysis_service import OrdersAnalysisService


class OrdersAnalysisServiceImpl(OrdersAnalysisService):

    def __init__(self):
        self.__ordersAnalysisRepository = OrdersAnalysisRepositoryImpl()

    async def readExcel(self):
        currentDirectory = os.getcwd()
        print(f"currentDirectory: {currentDirectory}") # 경로 파악

        filePath = os.path.join(
            currentDirectory, "..", "assets", "orders_data_after_drop_duplication.xlsx"
        )

        try:
            dataFrame = pd.read_excel(filePath)
            return dataFrame
        except FileNotFoundError:
            print(f"파일이 존재하지 않습니다.: {filePath}")


    async def trainModel(self):
        dataFrame = await self.readExcel()
        X_scaled, y, scaler = await self.__ordersAnalysisRepository.prepareViewCountVsQuantity(dataFrame)

        joblib.dump(scaler, "ordersModelScaler.pkl")

        X_train, X_test, y_train, y_test = await self.__ordersAnalysisRepository.splitTrainTestData(X_scaled, y)

        print(f"X_train: {X_train}, y_train: {y_train},"
              f"X_test: {X_test}, y_test: {y_test}")

        numberOfModels = 10
        modelList = []

        for index in range(numberOfModels):
            print(f"Training model {index + 1} / {numberOfModels}")

            model = await self.__ordersAnalysisRepository.createModel()

            await self.__ordersAnalysisRepository.fitModel(model, X_train, y_train)
            model.save(f"ordersModel_{index + 1}.h5")
            modelList.append(model)

        return f"Trained {numberOfModels} models 성공~!"

    async def predictQuantityFromModel(self, viewCount):
        print(f"predictQuantityFromModel -> viewCount: {viewCount}")

        scaler = joblib.load('ordersModelScaler.pkl')

        ordersPredictionList = []

        for index in range(1, 11):
            ordersModel = tf.keras.models.load_model(f"ordersModel_{index}.h5", custom_objects={'mse': 'mse'})
            X_pred = np.array([[viewCount]])
            X_pred_scaled = await self.__ordersAnalysisRepository.transformFromScaler(scaler, X_pred)

            ordersPredict = await self.__ordersAnalysisRepository.predictFromModel(ordersModel, X_pred_scaled)

            ordersPredictionList.append(float(ordersPredict)) # count를 int로 했지만 불러오다보면 float이 될 수 있어서 float 명시해줌

        averagePrediction = np.mean(ordersPredictionList)
        print(f"averagePrediction: {averagePrediction}")

        return averagePrediction