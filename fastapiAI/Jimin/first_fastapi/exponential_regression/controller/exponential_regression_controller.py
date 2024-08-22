from fastapi import APIRouter, Depends

from exponential_regression.service.exponential_regression_service_impl import ExponentialRegressionServiceImpl
from polynomialRegrssion.service.polynomial_regression_service_impl import PolynomialRegressionServiceImpl

exponentialRegressionRouter = APIRouter()

async def injectExponentialRegressionService() -> ExponentialRegressionServiceImpl:
    return ExponentialRegressionServiceImpl()


@exponentialRegressionRouter.get("/exponential-regression")
def exponentialRegression(exponentialRegressionService: ExponentialRegressionServiceImpl = Depends(injectExponentialRegressionService)):
    print(f"exponentialRegression()")
    return exponentialRegressionService.createSampleForExponentialRegression()