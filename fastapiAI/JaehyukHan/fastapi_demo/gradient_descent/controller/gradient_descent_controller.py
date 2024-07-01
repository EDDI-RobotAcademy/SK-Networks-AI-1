import os.path

import joblib
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from gradient_descent.entity.linear_regression_model import LinearRegressionModel
from gradient_descent.service.gradient_descent_service_impl import GradientDescentServiceImpl


gradientDescentRouter = APIRouter()


async def injectGradientDescentService() -> GradientDescentServiceImpl:
    return GradientDescentServiceImpl()


@gradientDescentRouter.get('/gradient-descent-train')
async def gradientDescentTrain(gradientDescentService: GradientDescentServiceImpl =
                               Depends(injectGradientDescentService)):
    print(f"controller -> gradientDescentTrain()")

    result = await gradientDescentService.gradientDescentTrain()

    return JSONResponse(content={'result': result}, status_code=status.HTTP_200_OK)

class RequestForm(BaseModel):


@gradientDescentRouter.post("/gradient-descent-predict")
async def gradientDescentPredict(gradientDescentService: GradientDescentServiceImpl =
                               Depends(injectGradientDescentService)):
    print(f"controller -> gradientDescentPredict()")
    if not os.path.join('linear_regression_model.npz'):
        return {'error': '모델 학습부터 시키세요!'}

    model = loadModel(modelPath)