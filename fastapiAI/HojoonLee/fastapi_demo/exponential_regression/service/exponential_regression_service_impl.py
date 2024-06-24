from exponential_regression.service.exponential_regression_service import ExponentialRegressionService
from exponential_regression.repository.exponential_regression_repository_impl import ExponentialRegressionRepositoryImpl
import numpy as np
class ExponentialRegressionServiceImpl(ExponentialRegressionService):

    def __init__(self):
        self.exponentialRegressionRepository = ExponentialRegressionRepositoryImpl()

    def createSampleData(self):
        np.random.seed(0)
        X = np.arange(1,100) # 1부터 100까지의 데이터를 만듦 X = [1, 2, ... 100]
        y = 2 * np.exp(0.1 * X) + np.random.normal(size=X.size)
        return X, y

    def createSampleForExponentialRegression(self):
        print("service -> createSampleForExponentialRegression()")
        X, y = self.createSampleData()

        return self.exponentialRegressionRepository.regressionAnalysis(X, y)
