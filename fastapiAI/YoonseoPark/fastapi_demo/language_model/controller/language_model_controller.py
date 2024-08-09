from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from language_model.controller.request_form.user_predict_request_form import UserPredictRequestForm
from language_model.service.language_model_service_impl import LanguageModelServiceImpl

languageModelRouter = APIRouter()

async def injectLanguageModelService() -> LanguageModelServiceImpl:
    return LanguageModelServiceImpl()

@languageModelRouter.post("/language-modeling")
async def operateLanguageModel(languageModelService: LanguageModelServiceImpl =
                                 Depends(injectLanguageModelService)):
    print(f"controller -> operateLanguageModel()")

    languageModelService.operateLanguageModel()
    # return JSONResponse(content=predictText, status_code=status.HTTP_200_OK)

@languageModelRouter.post("/predict-with-modeling-language")
async def predictModelingLanguage(userPredictRequestForm: UserPredictRequestForm,
                                  languageModelService: LanguageModelServiceImpl =
                                  Depends(injectLanguageModelService)):

    print(f"controller -> predictModelingLanguage()")
    predictText = languageModelService.predictWithModelingLanguage(userPredictRequestForm)

    return JSONResponse(content=predictText, status_code=status.HTTP_200_OK)
