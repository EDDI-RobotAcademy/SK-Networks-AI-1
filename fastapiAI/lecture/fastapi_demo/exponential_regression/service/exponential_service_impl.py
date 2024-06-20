from exponential_regression.service.exponential_service import ExponentialRegressionService


class ExponentialRegressionServiceImpl(ExponentialRegressionService):
    # def __init__(self):
    #     self.exponentialRegressionRepository = ExponentialRegressionRepositoryImpl()

    def createSampleForExponentialRegression(self):
        print("service -> createSampleForExponentialRegression()")
