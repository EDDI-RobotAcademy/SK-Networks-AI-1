from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from random_forest.service.random_forest_service_impl import RandomForestServiceImpl

randomForestRouter = APIRouter()

# 싱글톤 패턴을 사용하지 않고 inject를 통해 서비스 객체를 받아옴
async def injectRandomForestService() -> RandomForestServiceImpl:
    return RandomForestServiceImpl()

@randomForestRouter.get("/random-forest")
async def randomForestAnalysis(randomForestService: RandomForestServiceImpl =
                               Depends(injectRandomForestService)):
    result = randomForestService.randomForestAnalysis()  # 최종 결과
    return JSONResponse(content=result)   # json 형태, 내용은 result