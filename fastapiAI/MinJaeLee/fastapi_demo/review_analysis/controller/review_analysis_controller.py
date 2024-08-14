from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import JSONResponse

from review_analysis.service.review_analysis_service_impl import ReviewAnalysisServiceImpl

reviewAnalysisRouter = APIRouter()


async def injectReviewAnalysisService() -> ReviewAnalysisServiceImpl:
    return ReviewAnalysisServiceImpl()


@reviewAnalysisRouter.post("/review-train")
async def reviewTrain(reviewAnalysisService: ReviewAnalysisServiceImpl = Depends(injectReviewAnalysisService)):
    print(f"controller -> reviewTrain()")

    reviewAnalysisService.reviewAnalysis()

    return JSONResponse(content={"message": "Learning Process Complete"}, status_code=status.HTTP_200_OK)


# @reviewAnalysisRouter.post("/sentiment-analysis")
# async def sentimentAnalysis(userPredictRequestForm: UserReviewrequestForm,
#                             reviewAnalysisService: ReviewAnalysisServiceImpl = Depends(injectReviewAnalysisService)):
#     print(f"controller -> sentimentAnalysis()")
#
#     predictedResult = reviewAnalysisService.sentimentAnalysis(userReviewRequestForm)
#
#     return JSONResponse(content=predictedResult, status_code=status.HTTP_200_OK)
