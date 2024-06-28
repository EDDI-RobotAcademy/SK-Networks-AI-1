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
        currentDirectory = os.getcwd() # 코드에서 실행하고 있는 디렉토리
        print(f"currentDirectory: {currentDirectory}")

        # 협업할 때는 상대경로 사용 (" " 사이에 / 사용 금지 -> // 이런 형태가 됨)
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
        X_scaled, y, scaler = await self.__ordersAnalysisRepository.prepareViewCountVsQuantity(dataFrame)

        joblib.dump(scaler, "ordersModelScaler.pkl") # joblib: 저장하고자 하는 값 # pkl(피클): 데이터 저장할 때 쓰임

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
            await self.__ordersAnalysisRepository.fitModel(model, X_train, y_train) # 훈련된 모델
            print("is it pass fitModel()")
            model.save(f"ordersModel_{index + 1}.h5") # 앞에 경로가 없으면 os.cwd의 경로와 같음
            modelList.append(model) # 나중에 가져다 쓸 수 있도록 리스트로 저장

        return f"Trained {numberOfModels} models 성공!!"

    async def predictQuantityFromModel(self, viewCount):
        print(f"predictQuantityFromModel -> viewCount: {viewCount}")

        scaler = joblib.load('ordersModelScaler.pkl')
        print(f"after load scaler")

        ordersPredictionList = []

        for index in range(1, 11):
            ordersModel = tf.keras.models.load_model(f"ordersModel_{index}.h5")
            print(f"after load model")
            X_pred = np.array([[viewCount]])
            # transform을 해주기 위해 2차원으로 [[]] 해줌
            X_pred_scaled = await self.__ordersAnalysisRepository.transformFromScaler(scaler, X_pred)

            ordersPredict = await self.__ordersAnalysisRepository.predictFromModel(ordersModel, X_pred_scaled)
            ordersPredictionList.append(float(ordersPredict)) # 내부적으로 float이 될 수 있어서 float을 명시해줌

        # 평균 prediction
        averagePrediction = np.mean(ordersPredictionList)
        print(f"averagePrediction: {averagePrediction}")

        return averagePrediction
