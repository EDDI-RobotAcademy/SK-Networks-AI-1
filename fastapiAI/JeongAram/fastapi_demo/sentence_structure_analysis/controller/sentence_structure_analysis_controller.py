from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sentence_structure_analysis.controller.request_form.sentence_request_form import SentenceRequestForm
from sentence_structure_analysis.service.response.sentence_structure_analysis_service_impl import \
    SentenceStructureAnalysisServiceImpl

sentenceStructureAnalysisRouter = APIRouter()

async def injectSentenceStructureAnalysisService() -> SentenceStructureAnalysisServiceImpl:
    return SentenceStructureAnalysisServiceImpl()

@sentenceStructureAnalysisRouter.post("/sentence-tokenize")
async def sentenceTokenize(sentenceRequestForm: SentenceRequestForm,
                           sentenceStructureAnalysisService: SentenceStructureAnalysisServiceImpl =
                           Depends(injectSentenceStructureAnalysisService)):

    print(f"controller -> sentenceTokenize(): sentenceRequestForm: {sentenceRequestForm}")

    analyzedResult = sentenceStructureAnalysisService.sentenceTokenize(sentenceRequestForm.toSentenceRequest())
    return JSONResponse(content=analyzedResult, status_code=status.HTTP_200_OK)

@sentenceStructureAnalysisRouter.post("/word-tokenize")
async def wordTokenize(sentenceRequestForm: SentenceRequestForm,
                       sentenceStructureAnalysisService: SentenceStructureAnalysisServiceImpl =
                       Depends(injectSentenceStructureAnalysisService)):

    print(f"controller -> wordTokenize(): sentenceRequestForm: {sentenceRequestForm}")

    analyzedResult = sentenceStructureAnalysisService.wordTokenize(sentenceRequestForm.toSentenceRequest())
    return JSONResponse(content=analyzedResult, status_code=status.HTTP_200_OK)

@sentenceStructureAnalysisRouter.post("/sentence-analysis")
async def sentenceAnalysis(sentenceRequestForm: SentenceRequestForm,
                           sentenceStructureAnalysisService: SentenceStructureAnalysisServiceImpl =
                           Depends(injectSentenceStructureAnalysisService)):

    print(f"controller -> sentenceAnalysis(): sentenceRequestForm: {sentenceRequestForm}")

    analyzedResult = sentenceStructureAnalysisService.sentenceAnalysis(sentenceRequestForm.toSentenceRequest())
    return JSONResponse(content=analyzedResult, status_code=status.HTTP_200_OK)