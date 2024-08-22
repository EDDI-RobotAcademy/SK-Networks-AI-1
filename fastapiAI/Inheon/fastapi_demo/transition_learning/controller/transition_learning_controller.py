from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from transition_learning.controller.request_form.transition_learning_predict_request_form import \
    TransitionLearningPredictRequestForm
from transition_learning.service.transition_learning_service_impl import TransitionLearningServiceImpl

transitionLearningRouter = APIRouter()

async def injectTransitionLearningService() -> TransitionLearningServiceImpl:
    return TransitionLearningServiceImpl()


@transitionLearningRouter.post("/transition-learning-predict")
async def predictWithTransitionLearning(transitionLearningPredictReqeustForm: TransitionLearningPredictRequestForm,
                                        transitionLearningService: TransitionLearningServiceImpl =
                                        Depends(injectTransitionLearningService)):

    print(f"controller -> predictWithTransitionLearning(): "
          f"transitionLearningPredictRequestForm: {transitionLearningPredictReqeustForm}")

    predictedResult = transitionLearningService.predictText(transitionLearningPredictReqeustForm)

    return JSONResponse(content=predictedResult, status_code=status.HTTP_200_OK)