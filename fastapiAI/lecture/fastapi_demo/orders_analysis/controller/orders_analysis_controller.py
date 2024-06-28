from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from orders_analysis.service.orders_analysis_service_impl import OrdersAnalysisServiceImpl

ordersAnalysisRouter = APIRouter()


async def injectOrdersAnalysisService() -> OrdersAnalysisServiceImpl:
    return OrdersAnalysisServiceImpl()


@ordersAnalysisRouter.get("/orders-train")
async def ordersTrain(ordersAnalysisService: OrdersAnalysisServiceImpl =
                      Depends(injectOrdersAnalysisService)):

    print(f"ordersTrain()")

    try:
        result = await ordersAnalysisService.trainModel()
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
