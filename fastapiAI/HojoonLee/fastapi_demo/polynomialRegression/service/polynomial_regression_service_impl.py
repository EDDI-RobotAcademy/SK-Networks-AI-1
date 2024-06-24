import numpy as np

from polynomialRegression.repository.polynomial_regression_repository_impl import PolynomialRegressionRepositoryImpl
from polynomialRegression.service.polynomial_regression_service import PolynomialRegressionService


class PolynomialRegressionServiceImpl(PolynomialRegressionService):
    def __init__(self):
        self.polynomialRegressionRepository = PolynomialRegressionRepositoryImpl()

    async def generateSampleData(self): #  내부 function >> 굳이 service엔 구현 x (사전 정의된 계산을 하는 것이므로)
        np.random.seed(0)
        X = 2 - 3 * np.random.normal(0,1,100) # 0 ~ 1 사이의 100개 값
        print(f"X: {X}")
        y = X - 2 * (X ** 2) + np.random.normal(-3,3,100) # -3 ~ 3 사이의 100개 값
        X = X[:,np.newaxis] # [1,100]이었던 X를 >> [100,1]로 바꿈 >> 행렬 연산을 위함 (n x m) * (m x p)
        print(f"after X: {X}")
        return X,y

    async def createSampleForPolynomialRegression(self):
        X, y = await self.generateSampleData()
        # 만들어진 샘플 데이터 X, y로 다항회귀 분석을 맡김
        return self.polynomialRegressionRepository.regressionAnalysis(X, y)