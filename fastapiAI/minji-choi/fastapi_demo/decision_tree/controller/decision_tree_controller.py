import os.path

import joblib
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from gradient_descent.controller.request_form.predict_request_form import PredictRequestForm
from decision_tree.service.decision_tree_service_impl import DecisionTreeServiceImpl

decisionTreeRouter = APIRouter()


async def injectDecisionTreeService() -> DecisionTreeServiceImpl:
    return DecisionTreeServiceImpl()


@decisionTreeRouter.get("/decision-tree-train")
async def decisionTreeTrain(decisionTreeService: DecisionTreeServiceImpl =
                               Depends(injectDecisionTreeService)):

    print(f"controller -> decisionTreeTrain()")

    decisionTreeService.decisionTreeTrain()
    # return JSONResponse(content={"result":result}, status_code=status.HTTP_200_OK)
#
# @decisionTreeRouter.post("/decision-tree-predict")
# async def decisionTreePredict(requestForm: PredictRequestForm,
#                                  decisionTreeService: DecisionTreeServiceImpl =
#                                  Depends(injectDecisionTreeService)):
#
#     print(f"controller -> decisionTreePredict()")
#     predictions = await decisionTreeService.decisionTreePredict(requestForm.toPredictRequest()) # result =
#
#     return JSONResponse(content={"predictions":predictions}, status_code=status.HTTP_200_OK)
#
