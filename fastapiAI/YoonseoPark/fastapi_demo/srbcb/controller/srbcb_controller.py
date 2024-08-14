from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from srbcb.controller.request_form.srbcb_request_form import SrbcbRequestForm
from srbcb.service.srbcb_service_impl import SrbcbServiceImpl

srbcbRouter = APIRouter()

# Simple Rule Base Chat Bot
async def injectSrbcbService() -> SrbcbServiceImpl:
    return SrbcbServiceImpl()

@srbcbRouter.post("/srbcb-response")
async def srbcbTrain(srbcbRequestForm: SrbcbRequestForm,
                           srbcbService: SrbcbServiceImpl = Depends(injectSrbcbService)):

    print(f"controller -> srbcbTrain(): srbcbRequestForm: {srbcbRequestForm}")

    generatedText = srbcbService.ruleBaseResponse(srbcbRequestForm.userSendMessage)
    return JSONResponse(content={"generatedText": generatedText}, status_code=status.HTTP_200_OK)