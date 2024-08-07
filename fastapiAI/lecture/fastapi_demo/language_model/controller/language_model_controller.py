from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import JSONResponse

from language_model.service.language_model_service_impl import LanguageModelServiceImpl

languageModelRouter = APIRouter()

async def injectLanguageModelService() -> LanguageModelServiceImpl:
    return LanguageModelServiceImpl()

@languageModelRouter.post("/language-modeling")
async def operateLanguageModel(languageModelService: LanguageModelServiceImpl =
                               Depends(injectLanguageModelService)):

    print(f"controller -> operateLanguageModel()")

    languageModelService.operateLanguageModel()

    # return JSONResponse(content=predictedNextSequence, status_code=status.HTTP_200_OK)
