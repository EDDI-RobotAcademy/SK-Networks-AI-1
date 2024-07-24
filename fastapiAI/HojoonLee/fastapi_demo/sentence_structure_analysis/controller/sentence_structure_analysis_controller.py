from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sentence_structure_analysis.controller.request_form.sentence_request_form import SentenceRequestForm
from sentence_structure_analysis.service.sentence_structure_analysis_service_impl import \
    SentenceStructureAnalysisServiceImpl

sentenceStructureAnalysisRouter = APIRouter()

async def injectSentenceStructureAnalysisSerivce() -> SentenceStructureAnalysisServiceImpl:
    return SentenceStructureAnalysisServiceImpl()

@sentenceStructureAnalysisRouter.post("/sentence-tokenize")
async def sentenceTokenize(sentenceRequsetForm: SentenceRequestForm,
                           sentenceStructureAnalysisService: SentenceStructureAnalysisServiceImpl =
                           Depends(injectSentenceStructureAnalysisSerivce)):
    # 여러 문장을 문장 단위로 쪼개기
    print(f"controller -> sentenceTokenize(): sentenceRequestForm: {sentenceRequsetForm}")

    # contorller -> request_form(toSentenceRequest() 실행) -> 포맷 바꾼 상태로 service로 감
    analyzedResult = sentenceStructureAnalysisService.sentenceTokenize(sentenceRequsetForm.toSentenceRequest())
    return JSONResponse(content=analyzedResult, status_code=status.HTTP_200_OK)

@sentenceStructureAnalysisRouter.post("/word-tokenize")
async def wordTokenize(sentenceRequsetForm: SentenceRequestForm,
                       sentenceStructureAnalysisService: SentenceStructureAnalysisServiceImpl =
                       Depends(injectSentenceStructureAnalysisSerivce)):

    # 문장을 단어 단위로 쪼개기 -> prompt에서 활용가능 빈도수 count용으로
    print(f"controller -> wordTokenize(): sentenceRequestForm: {sentenceRequsetForm}")

    analyzedResult = sentenceStructureAnalysisService.wordTokenize(sentenceRequsetForm.toSentenceRequest())
    return JSONResponse(content=analyzedResult, status_code=status.HTTP_200_OK)

@sentenceStructureAnalysisRouter.post("/sentence-analysis")
async def sentenceAnalysis(sentenceRequsetForm: SentenceRequestForm,
                       sentenceStructureAnalysisService: SentenceStructureAnalysisServiceImpl =
                       Depends(injectSentenceStructureAnalysisSerivce)):

    # 단어의 품사를 분석함
    print(f"controller -> sentenceAnalysis(): sentenceRequestForm: {sentenceRequsetForm}")

    analyzedResult = sentenceStructureAnalysisService.sentenceAnalysis(sentenceRequsetForm.toSentenceRequest())
    return JSONResponse(content=analyzedResult, status_code=status.HTTP_200_OK)