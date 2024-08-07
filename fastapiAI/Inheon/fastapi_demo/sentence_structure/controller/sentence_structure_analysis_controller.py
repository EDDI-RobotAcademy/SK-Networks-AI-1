from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sentence_structure.controller.request_form.sentence_request_form import SentenceRequestForm
from sentence_structure.service.sentence_structure_analysis_service_impl import SentenceStructureAnalysisServiceImpl

sentenceStructureAnalysisRouter = APIRouter()


async def injectSentenceStructureAnalysisService() -> SentenceStructureAnalysisServiceImpl:
    return SentenceStructureAnalysisServiceImpl()

@sentenceStructureAnalysisRouter.post('/sentence-tokenize')
async def sentenceTokenize(sentenceRequestForm: SentenceRequestForm,
                           sentenceStructureAnalysisService: SentenceStructureAnalysisServiceImpl =
                           Depends(injectSentenceStructureAnalysisService)):

    print(f"controller -> sentenceTokenize(): sentenceRequestForm: {sentenceRequestForm}")

    analyzedResult = sentenceStructureAnalysisService.sentenceTokenize(sentenceRequestForm.toSentenceRequest())
    return JSONResponse(content=analyzedResult, status_code=status.HTTP_200_OK)

@sentenceStructureAnalysisRouter.post('/word-tokenize')
async def wordTokenize(sentenceReqeustForm: SentenceRequestForm,
                       sentenceStructureAnalysisService: SentenceStructureAnalysisServiceImpl =
                       Depends(injectSentenceStructureAnalysisService)):

    print(f'controller -> wordTokenize(): sentenceRequestForm: {sentenceReqeustForm}')

    analyzedResult = sentenceStructureAnalysisService.wordTokenize(sentenceReqeustForm.toSentenceRequest())
    return JSONResponse(content=analyzedResult, status_code=status.HTTP_200_OK)

@sentenceStructureAnalysisRouter.post('/sentence-analysis')
async def sentenceAnalysis(sentenceReqeustForm: SentenceRequestForm,
                       sentenceStructureAnalysisService: SentenceStructureAnalysisServiceImpl =
                       Depends(injectSentenceStructureAnalysisService)):

    print(f'controller -> sentenceAnalysis(): sentenceRequestForm: {sentenceReqeustForm}')

    analyzedResult = sentenceStructureAnalysisService.sentenceAnalysis(sentenceReqeustForm.toSentenceRequest())
    return JSONResponse(content=analyzedResult, status_code=status.HTTP_200_OK)