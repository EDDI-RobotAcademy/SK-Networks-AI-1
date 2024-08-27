from fastapi import APIRouter, Depends,status
from fastapi.responses import JSONResponse

from langchain_interconnect.controller.request_form.langchain_request_form import LangchainRequestForm
from langchain_interconnect.service.langchain_service_impl import LangchainServiceImpl

langchainRouter = APIRouter()

async def injectLangchainService():
    return LangchainServiceImpl()

@langchainRouter.post("/rag-based-question")
async def ragWithLangChain(langchainRequestForm: LangchainRequestForm,
                           langchainService: LangchainServiceImpl =
                           Depends(injectLangchainService)):

    print(f"controller -> ragWithLangChain(): langchainRequestForm: {langchainRequestForm}")

    result = await langchainService.ragWithLangChain(langchainRequestForm.userSendMessage)

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
