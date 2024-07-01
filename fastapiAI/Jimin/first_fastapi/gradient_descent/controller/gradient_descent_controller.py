import os

from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from gradient_descent.controller.request_form.predict_reqeust_form import PredictRequestForm
from gradient_descent.entity.linear_regression_model import LinearRegressionModel
from gradient_descent.service.gradient_descent_service_impl import GradientDescentServiceImpl
import numpy as np
import tensorflow as tf


gradientDescentRouter = APIRouter()

async def injectGradientDescentService() -> GradientDescentServiceImpl:
    return GradientDescentServiceImpl()


@gradientDescentRouter.get("/gradient-descent-train")
async def gradientDescentTrain(gradientDescentService: GradientDescentServiceImpl = Depends(injectGradientDescentService)):
    print(f"controller -> gradientDescentTrain()")

    result = await gradientDescentService.gradientDescentTrain()
    return JSONResponse(content={"result": result}, status_code=status.HTTP_200_OK)



@gradientDescentRouter.post("/gradient-descent-predict")
async def gradientDescentPredict(requestForm: PredictRequestForm,
                                 gradientDescentService: GradientDescentServiceImpl = Depends(injectGradientDescentService)):

    print(f"controller -> gradientDescentPredict()")
    # requestform이 복잡히 올 수가 있다.
    # 각 도메인별로 구성해서 날아갈 수 있도록 해주는게 toPredictRequest이다.
    predictions = await gradientDescentService.gradientDescentPredict(requestForm.toPredictReqeust())
    return JSONResponse(content={"predictions": predictions}, status_code=status.HTTP_200_OK)

