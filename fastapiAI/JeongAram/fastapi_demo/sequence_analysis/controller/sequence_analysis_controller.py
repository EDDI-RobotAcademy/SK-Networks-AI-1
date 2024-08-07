from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sequence_analysis.controller.request_form.sequence_analysis_request_form import SequenceAnalysisRequestForm
from sequence_analysis.service.sequence_analysis_service_impl import SequenceAnalysisServiceImpl

sequenceAnalysisRouter = APIRouter()

async def injectSequenceAnalysisService() -> SequenceAnalysisServiceImpl():
    return SequenceAnalysisServiceImpl()

@sequenceAnalysisRouter.post("/predict-next-sequence")
async def predictNextSequence(sequenceAnalysisRequestForm: SequenceAnalysisRequestForm,
                              sequenceAnalysisService: SequenceAnalysisServiceImpl =
                              Depends(injectSequenceAnalysisService)):

    print(f"controller -> predictNextSequence(): sequenceAnalysisRequestForm: {sequenceAnalysisRequestForm}")

    predictNextSequence = sequenceAnalysisService.predictNextSequence(
        sequenceAnalysisRequestForm.userSendMessage)
    return JSONResponse(content=predictNextSequence, status_code=status.HTTP_200_OK)