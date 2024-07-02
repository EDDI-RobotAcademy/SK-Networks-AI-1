import numpy as np

from polynomialRegression.repository.polynomial_regression_repository_impl import PolynomialRegressionRepositoryImpl
from polynomialRegression.service.polynomial_regression_service import PolynomialRegressionService


class PolynomialRegressionServiceImpl(PolynomialRegressionService):
    def __init__(self):
        self.polynomialRegressionRepository = PolynomialRegressionRepositoryImpl()
    async def generateSampleData(self):
        np.random.seed(0)
        X = 2 - 3 * np.random.normal(0,1,100)
        y = X - 2 * (X**2) + np.random.normal(-3,3,100)
        print(f"X: {X}")
        X = X[:, np.newaxis]
        print(f"after X : {X}")
        return X,y
    async def createSampleForPolynomialRegression(self):
        X, y = await self.generateSampleData()
        return self.polynomialRegressionRepository.regressionAnalysis(X, y)

