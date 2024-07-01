import os.path

import joblib
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from gradient_descent.entity.linear_regression_model import LinearRegressionModel
from gradient_descent.service.gradient_descent_service_impl import GradientDescentServiceImpl

import numpy as np
import tensorflow as tf

gradientDescentRouter = APIRouter()


async def injectGradientDescentService() -> GradientDescentServiceImpl:
    return GradientDescentServiceImpl()


@gradientDescentRouter.get("/gradient-descent-train")
async def gradientDescentTrain(gradientDescentService: GradientDescentServiceImpl =
                               Depends(injectGradientDescentService)):

    print(f"controller -> gradientDescentTrain()")

    result = await gradientDescentService.gradientDescentTrain()

    return JSONResponse(content={"result": result}, status_code=status.HTTP_200_OK)

class PredictRequest(BaseModel):
    X: list

@gradientDescentRouter.post("/gradient-descent-predict")
async def gradientDescentPredict(request: PredictRequest):
    if not os.path.exists('linear_regression_model.npz'):
        return {"error": "모델 학습부터 시키세요!"}

    # model = loadModel('linear_regression_model.npz')
    # X_new = tf.constant(request.X, dtype=tf.float32)
    # predictions = model(X_new).numpy().tolist()
    #
    # return {"predictions": predictions}

