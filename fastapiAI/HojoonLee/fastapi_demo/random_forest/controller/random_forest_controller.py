# random forest는 데이터가 불규칙(불균형)한 경우 효과가 있음
# 오히려 균형이 있으면 효과가 없음

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from random_forest.service.random_forest_service_impl import RandomForestServiceImpl

randomForestRouter = APIRouter()

async def injectRandomForestService() -> RandomForestServiceImpl:
    return RandomForestServiceImpl()

@randomForestRouter.get("/random-forest")
async def randomForestAnalysis(randomForestService: RandomForestServiceImpl =
                                Depends(injectRandomForestService)):
        result = randomForestService.randomForestAnalysis()
        return JSONResponse(content=result)