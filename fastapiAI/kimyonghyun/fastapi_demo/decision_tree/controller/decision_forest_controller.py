import os.path

import joblib
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from decision_tree.service.decision_tree_service_impl import DecisionTreeServiceImpl
from gradient_descent.controller.request_form.predict_request_form import PredictRequestForm
from gradient_descent.entity.linear_regression_model import LinearRegressionModel
from gradient_descent.service.gradient_descent_service_impl import GradientDescentServiceImpl

import numpy as np
import tensorflow as tf

decisionTreeRouter = APIRouter()


async def injectDecisionTreeService() -> DecisionTreeServiceImpl:
    return DecisionTreeServiceImpl()


@decisionTreeRouter.get("/Decision-Tree")
async def decisionTreeTrain(decisionTreeService: DecisionTreeServiceImpl =
                               Depends(injectDecisionTreeService)):

    print(f"controller -> decisionTreeTrain()")

    decisionTreeService.decisionTreeTrain()

    # result = await decisionTreeService.decisionTreeTrain()

    # return JSONResponse(content={"result": result}, status_code=status.HTTP_200_OK)


# @decisionTreeRouter.post("/gradient-descent-predict")
# async def decisionTreePredict(requestForm: PredictRequestForm,
#                                  gradientDescentService: GradientDescentServiceImpl =
#                                  Depends(injectDecisionTreeService)):
#
#     print(f"controller -> gradientDescentPredict()")
#
#     predictions = await gradientDescentService.gradientDescentPredict(requestForm.toPredictRequest())
#
#     return JSONResponse(content={"predictions": predictions}, status_code=status.HTTP_200_OK)