import os.path

import joblib
import numpy as np
import tensorflow as tf
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from gradient_descent.controller.request_form.predict_request_form import PredictRequestForm
from gradient_descent.entity.linear_regression_model import LinearRegressionModel
from gradient_descent.service.gradient_descent_service_impl import GradientDescentServiceImpl


gradientDescentRouter = APIRouter()

async def injectGraientDescentService() -> GradientDescentServiceImpl:
    return GradientDescentServiceImpl()

@gradientDescentRouter.get("/gradient-descent-train")
async def gradientDescentTrain(gradientDescentService: GradientDescentServiceImpl =
                               Depends(injectGraientDescentService)):

    print(f"controller -> gradientDescentTrain()")

    result = await gradientDescentService.gradientDescentTrain()

    return JSONResponse(content={"result": result}, status_code=status.HTTP_200_OK)


@gradientDescentRouter.post("/gradient-descent-predict")
async def gradientDescentPredict(requestForm: PredictRequestForm,
                                 gradientDescentService: GradientDescentServiceImpl =
                                 Depends(injectGraientDescentService)):

    print(f"controller -> gradientDescentPredict()")

    # requestForm을
    predictions = await gradientDescentService.gradientDescentPredict(requestForm.toPredictRequest())

    return JSONResponse(content={"predictions": predictions}, status_code=status.HTTP_200_OK)



