import numpy as np

from polynomialRegression.repository.polynomial_regression_repository_impl import PolynomialRegressionRepositoryImpl
from polynomialRegression.service.polynomial_regression_service import PolynomialRegressionService


class PolynomialRegressionServiceImpl(PolynomialRegressionService):
    def __init__(self):
        self.polynomialRegressionRepository = PolynomialRegressionRepositoryImpl()

    async def generateSampleData(self):
        np.random.seed(0)
        X = 2-3 * np.random.normal(0,1,100)
        # print(f"X:{X}")
        y = X - 2 * (X**2) + np.random.normal(-3, 3, 100)
        # print(f"y:{y}")
        X = X[:, np.newaxis]
        # print(f"ager X: {X}")

        # 행렬의 연산 조건 (n x m) . (k x p)
        # 기본적으로 m과 k가 일치해야 연산 할 수 있으므로 차원 이동 시킨 것
        # 물론 수도 행렬은 저거 안맞아도 할수 있긴 하지만 이건 너무 넘어감
        return X, y
    async def createSampleForPolynomialRegression(self):
        X, y = await self.generateSampleData()
        return self.polynomialRegressionRepository.regressionAnalysis(X,y)