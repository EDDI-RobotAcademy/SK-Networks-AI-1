from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from polynomialRegression.service.polynomial_regression_service_impl import PolynomialRegressionServiceImpl

polynomialRegressionRouter = APIRouter()

polynomialRegressionService = PolynomialRegressionServiceImpl()

async def injectPolynomialRegressionService() -> PolynomialRegressionServiceImpl:
    return PolynomialRegressionServiceImpl()


@polynomialRegressionRouter.get("/polynomial-regression",)
async def polynomialRegression(polynomialRegressionService: PolynomialRegressionServiceImpl =
                               Depends(injectPolynomialRegressionService)):
    X, y, X_new, y_pred = await polynomialRegressionService.createSampleForPolynomialRegression()

    return {
        "X": X,
        "y": y,
        "X_new": X_new,
        "y_pred": y_pred
    }
