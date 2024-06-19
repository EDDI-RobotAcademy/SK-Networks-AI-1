from polynomialRegression.repository.polynomial_regression_repository_impl import PolynomialRegressionRepositoryImpl
from polynomialRegression.service.polynomial_regression_service import PolynomialRegressionService


class PolynomialRegressionServiceImpl(PolynomialRegressionService):
    def __init__(self):
        self.polynomialRegressionRepository = PolynomialRegressionRepositoryImpl()

    async def polynomialRegression(self):
        return self.polynomialRegressionRepository.regressionAnalysis()
