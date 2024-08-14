from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import JSONResponse

from openai_basic.controller.request_form.openai_talk_request_form import OpenAITalkRequestForm
from openai_basic.service.openai_basic_service_impl import OpenAIBasicServiceImpl

openAIBasicRouter = APIRouter()

async def injectOpenAIBasicService() -> OpenAIBasicServiceImpl:
    return OpenAIBasicServiceImpl()

@openAIBasicRouter.post("/lets-talk")
async def talkWithOpenAI(openAITalkRequestForm: OpenAITalkRequestForm,
                         openAIBasicService: OpenAIBasicServiceImpl =
                         Depends(injectOpenAIBasicService)):

    print(f"controller -> talkWithOpenAI(): openAITalkRequestForm: {openAITalkRequestForm}")

    openAIGeneratedText = await openAIBasicService.letsTalk(openAITalkRequestForm.userSendMessage)

    return JSONResponse(content=openAIGeneratedText, status_code=status.HTTP_200_OK)
