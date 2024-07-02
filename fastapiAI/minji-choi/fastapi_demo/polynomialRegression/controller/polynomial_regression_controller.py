from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from polynomialRegression.service.polynomial_regression_service_impl import PolynomialRegressionServiceImpl
from train_test_evaluation.controller.response_form.analysis_result_response_form import AnalysisResultResponseForm

polynomialRegressionRouter = APIRouter()

async def injectPolynomialRegressionService() -> PolynomialRegressionServiceImpl:
    return PolynomialRegressionServiceImpl()


@polynomialRegressionRouter.get("/polynomial-regression",)
async def polynomialRegression(polynomialRegressionService: PolynomialRegressionServiceImpl =
                               Depends(injectPolynomialRegressionService)):
    X, y, X_new, y_pred = await polynomialRegressionService.createSampleForPolynomialRegression()
    await polynomialRegressionService.createSampleForPolynomialRegression()

    return {
        "X": X,
        "y": y,
        "X_new": X_new,
        "y_pred": y_pred,
    }


