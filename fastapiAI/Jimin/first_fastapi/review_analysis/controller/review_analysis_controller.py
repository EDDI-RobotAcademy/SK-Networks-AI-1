from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from review_analysis.controller.request_form.review_analysis_request_form import UserReviewRequestForm
from review_analysis.service.review_analysis_service_impl import ReviewAnalysisServiceImpl

reviewAnalysisRouter = APIRouter()

async def injectReviewAnalysisService() -> ReviewAnalysisServiceImpl:
    return ReviewAnalysisServiceImpl()

@reviewAnalysisRouter.post("/review-train")
async def reviewTrain(reviewAnalysisService: ReviewAnalysisServiceImpl =
                      Depends(injectReviewAnalysisService)):

    print(f"controller -> reviewTrain()")

    reviewAnalysisService.reviewAnalysis()

    return JSONResponse(content={"message": "학습이 완료되었습니다."}, status_code=status.HTTP_200_OK)

@reviewAnalysisRouter.post("/sentiment-analysis")
async def sentimentAnalysis(userReviewRequestForm: UserReviewRequestForm,
                            reviewAnalysisService: ReviewAnalysisServiceImpl =
                            Depends(injectReviewAnalysisService)):

    print(f"controller -> sentimentAnalysis()")

    predictedResult = reviewAnalysisService.sentimentAnalysis(userReviewRequestForm)

    return JSONResponse(content=predictedResult, status_code=status.HTTP_200_OK)