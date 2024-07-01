import joblib
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from gradient_descent.service.gradient_descent_service_impl import GradientDescentServiceImpl

gradientDescentRouter = APIRouter()


async def injectGradientDescentService() -> GradientDescentServiceImpl:
    return GradientDescentServiceImpl()


@gradientDescentRouter.get("/gradient-descent-train")
async def gradientDescentTrain(gradientDescentService: GradientDescentServiceImpl =
                               Depends(injectGradientDescentService)):

    print(f"controller -> gradientDescentTrain()")

    gradientDescentService.gradientDescentTrain()
