import numpy as np
from exponential_regression.service.exponential_service import ExponentialRegressionService
from exponential_regression.repository.exponential_regression_repository_impl import ExponentialRegressionRepositoryImpl


class ExponentialRegressionServiceImpl(ExponentialRegressionService):

    def __init__(self):
        self.exponentialRegressionRepository = ExponentialRegressionRepositoryImpl()
    def createSampleData(self):
        np.random.seed(0)
        X = np.arange(1, 100)
        y = 2 * np.exp(0.1 * X) + np.random.normal(size=X.size)
        return X, y

    def createSampleForExponentialRegression(self):
        print('service -> createSampleForExponentialRegression()')
        X, y = self.createSampleData()
        print('X: ', X)
        print('y: ', y)
        return self.exponentialRegressionRepository.regressionAnalysis(X, y)