from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from random_forest.service.random_forest_service_impl import RandomForestServiceImpl

randomForestRouter = APIRouter()


async def injectRandomForestService() -> RandomForestServiceImpl:
    return RandomForestServiceImpl()


@randomForestRouter.get('/random-forest')
async def randomForestAnalysis(randomForestService: RandomForestServiceImpl =
                               Depends(injectRandomForestService)):
    result = randomForestService.randomForestAnalysis()
    return JSONResponse(content=result)

