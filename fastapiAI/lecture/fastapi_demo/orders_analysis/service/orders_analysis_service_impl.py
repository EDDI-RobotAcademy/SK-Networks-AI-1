import os

import joblib
import pandas as pd

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

        X_train, y_train, X_test, y_test = \
            await self.__ordersAnalysisRepository.splitTrainTestData(X_scaled, y)
        print(f"X_train: {X_train}, y_train: {y_train},"
              f"X_test: {X_test}, y_test: {y_test}")
