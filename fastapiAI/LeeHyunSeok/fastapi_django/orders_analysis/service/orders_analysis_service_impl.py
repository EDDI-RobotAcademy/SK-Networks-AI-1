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

    async def readExcel(self):   #assets에 있는 orders_data_after_drop_duplication 엑셀파일을 읽어오는 코드
        currentDirectory = os.getcwd()   # os.getcwd()는 지금 코드가 돌아가는 디렉토리를 뜻함
        print(f"currentDirectory: {currentDirectory}")


        # 이 방법은 상대경로로 찾는 방법임/ ".."은 한 단계 위 디렉토리 / currentDirectory는 '/'의 역할을 해주므로 /는 생략해줘도 된다. 만약 /를 붙이면 //이렇게 되는 거임
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

        joblib.dump(scaler, "ordersModelScaler.pkl")   #joblib은 어떤 값을 저장하는 기능

        X_train, X_test, y_train, y_test = \
            await self.__ordersAnalysisRepository.splitTrainTestData(X_scaled, y)
        print(f"X_train: {X_train}, y_train: {y_train},"
              f"X_test: {X_test}, y_test: {y_test}")

        numberOfModels = 10
        modelList = []      # 나중에 list로 쓸일을 대비해서 list에 저장

        for index in range(numberOfModels):
            print(f"Training model {index + 1} / {numberOfModels}")

            model = await self.__ordersAnalysisRepository.createModel()
            print("is it pass createModel()")
            await self.__ordersAnalysisRepository.fitModel(model, X_train, y_train)
            print("is it pass fitModel()")
            model.save(f"ordersModel_{index + 1}.h5")       # h5는 텐서플로우에서 사용하는 확장자
            modelList.append(model)

        return f"Trained {numberOfModels} models 성공~~!!~!"

    async def predictQuantityFromModel(self, viewCount):        # 예측을 하는 부분
        print(f"predictQuantityFromModel -> viewCount: {viewCount}")

        scaler = joblib.load('ordersModelScaler.pkl')
        print(f"after load scaler")

        ordersPredictionList = [] # 밑에서 10번을 돌면서 평균을 내서 저장하려고 변수 생성

        for index in range(1, 11):
            print(f"ordersModel_{index}.h5")
            ordersModelFileName = f"ordersModel_{index}.h5"     #
            ordersModel = tf.keras.models.load_model(f"./{ordersModelFileName}", compile=True)
            print(f"after load model")
            X_pred = np.array([[viewCount]])    # [[]]로 받은 이유는 transform을 해주기 위해서이다.(2차원으로 받기 위해서.)
            X_pred_scaled = await self.__ordersAnalysisRepository.transformFromScaler(scaler, X_pred)

            ordersPredict = await self.__ordersAnalysisRepository.predictFromModel(
                ordersModel, X_pred_scaled)

            ordersPredictionList.append(float(ordersPredict))

        averagePrediction = np.mean(ordersPredictionList)
        print(f"averagePrediction: {averagePrediction}")

        return averagePrediction