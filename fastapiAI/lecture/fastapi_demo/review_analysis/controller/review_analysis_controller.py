from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import JSONResponse

from review_analysis.service.review_analysis_service_impl import ReviewAnalysisServiceImpl

reviewAnalysisRouter = APIRouter()

async def injectReviewAnalysisService() -> ReviewAnalysisServiceImpl:
    return ReviewAnalysisServiceImpl()

@reviewAnalysisRouter.post("/review-train")
async def reviewTrain(reviewAnalysisService: ReviewAnalysisServiceImpl =
                      Depends(injectReviewAnalysisService)):

    print(f"controller -> reviewTrain()")

    reviewAnalysisService.reviewAnalysis()

    return JSONResponse(content={"message": "학습이 완료되었습니다"}, status_code=status.HTTP_200_OK)
