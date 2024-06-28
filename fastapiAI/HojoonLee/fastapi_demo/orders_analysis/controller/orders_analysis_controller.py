from typing import List

import joblib
from aiomysql import Pool
from fastapi import APIRouter, Depends, HTTPException, status
from async_db.database import getMySqlPool
from fastapi.responses import JSONResponse

from orders_analysis.controller.request_form.view_count_request_form import ViewCountRequestForm
from orders_analysis.service.orders_analysis_service_impl import OrdersAnalysisServiceImpl

OrdersAnalysisRouter = APIRouter()


async def injectOrdersAnalysisService() -> OrdersAnalysisServiceImpl:
    return OrdersAnalysisServiceImpl()

@OrdersAnalysisRouter.get("/orders-train")
async def ordersTrain(ordersAnalysisService: OrdersAnalysisServiceImpl =
                                Depends(injectOrdersAnalysisService)):

    print(f"ordersTrain()")

    try:
        result = await ordersAnalysisService.trainModel()
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@OrdersAnalysisRouter.post("/orders-predict")
async def ordersPredict(request: ViewCountRequestForm,
                        ordersAnalysisService: OrdersAnalysisServiceImpl =
                        Depends(injectOrdersAnalysisService)):

    try:
        print(f"request: {request}")

        predictedQuantity = await ordersAnalysisService.predictQuantityFromModel(request.count)
        return JSONResponse(content=predictedQuantity, status_code=status.HTTP_200_OK)

    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Model File이 없음")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))