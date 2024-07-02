from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from gradient_descent.controller.request_form.predict_request_form import PredictRequestForm
from gradient_descent.service.gradient_descent_service_ipml import GradientDescentServiceImpl

gradientDescentRouter = APIRouter()

class PredictRequest(BaseModel):
    X: list

async def injectGradientDescentService() -> GradientDescentServiceImpl:
    return GradientDescentServiceImpl()

@gradientDescentRouter.get("/gradient-descent-train")
async def gradientDescentTrain(gradientDescentService: GradientDescentServiceImpl =
                                Depends(injectGradientDescentService)):

    print(f"gradientDescentTrain()")
    result = await gradientDescentService.gradientDescentTrain()
    # status vs status_code ?
    return JSONResponse(content={"result":result}, status_code=status.HTTP_200_OK)

@gradientDescentRouter.post("/gradient-descent-predict")
async def gradientDescentPredict(requestForm: PredictRequestForm,
                                 gradientDescentService: GradientDescentServiceImpl =
                                 Depends(injectGradientDescentService)):

    # requestForm을 request화 해서 보내기 (다중 도메인에 보내기 위함)
    predictions = await gradientDescentService.gradientDescentPredict(requestForm.toPredictRequest())

    return JSONResponse(content={"predictions":predictions}, status_code=status.HTTP_200_OK)





