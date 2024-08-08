from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from tf_idf_bow.controller.request_form.tf_idf_bow_request_form import TfIdfBowRequestForm
from tf_idf_bow.service.tf_idf_bow_service_impl import TfIdfBowServiceImpl

tfIdfBowRouter = APIRouter()

async def injectTfIdfBowService() -> TfIdfBowServiceImpl:
    return TfIdfBowServiceImpl()

@tfIdfBowRouter.post('/find-similarity-document')
async def findSimilarityDocument(tfIdfBowRequestForm: TfIdfBowRequestForm,
                                 tfIdfBowService: TfIdfBowServiceImpl = Depends(injectTfIdfBowService)):
    print(f'controller -> findSimilarityDocument(): tfIdfBowRequestForm: {tfIdfBowRequestForm}')
    foundSimilarityDocumentList = tfIdfBowService.findSimilarDocumentList(tfIdfBowRequestForm.userSendMessage)
    return JSONResponse(content = foundSimilarityDocumentList, status_code=status.HTTP_200_OK)