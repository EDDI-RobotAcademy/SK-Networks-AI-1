from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from polynomialRegression.service.polynomial_regression_service_impl import PolynomialRegressionServiceImpl

polynomialRegressionRouter = APIRouter()

# Dependency Injection On Asynchronous Framework

async def injectPolynomialRegressionService() -> PolynomialRegressionServiceImpl:
    return PolynomialRegressionServiceImpl()

polynomialRegressionService = PolynomialRegressionServiceImpl()

@polynomialRegressionRouter.get("/polynomial-regression")
async def polynomialRegression(polynomialRegressionService:PolynomialRegressionServiceImpl =
                                Depends(injectPolynomialRegressionService)):
    #await polynomialRegressionService.createSampleForPolynomialRegression()
    # ddd 방식으로 다항회귀식을 맡기고 결과 값들을 반환
    X,y,X_new,y_pred = await polynomialRegressionService.createSampleForPolynomialRegression()

    # 다항회귀 모델에 의한 X,y 값 client에게 보냄
    return {
        "X": X,
        "y": y,
        "X_new": X_new,
        "y_pred": y_pred
    }