from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from exponential_regression.service.exponential_regression_service_impl import ExponentialRegressionServiceImpl

exponentialRegressionRouter = APIRouter()


async def injectExponentialRegressionService() -> ExponentialRegressionServiceImpl:
    return ExponentialRegressionServiceImpl()


@exponentialRegressionRouter.get("/exponential-regression")
async def exponentialRegression(exponentialRegressionService: ExponentialRegressionServiceImpl =
                                Depends(injectExponentialRegressionService)):

    print(f"exponentialRegression()")
    return exponentialRegressionService.createSampleForExponentialRegression()
