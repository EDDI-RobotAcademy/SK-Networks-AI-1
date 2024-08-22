from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from transition_learning.controller.request_form.gpt2_pretrained_prediction_request_form import \
    GPT2PretrainedPredictionRequestForm
from transition_learning.controller.request_form.sentiment_analysis_request_form import SentimentAnalysisRequestForm
from transition_learning.controller.request_form.transition_learning_request_form import TransitionLearningRequestForm
from transition_learning.service.transition_learning_service_impl import TransitionLearningServiceImpl

transitionLearningRouter = APIRouter()

async def injectTransitionLearningService() -> TransitionLearningServiceImpl:
    return TransitionLearningServiceImpl()

@transitionLearningRouter.post("/transition-learning-predict")
async def predictWithTransitionLearning(transitionLearningPredictRequestForm: TransitionLearningRequestForm,
                                        transitionLearningService: TransitionLearningServiceImpl =
                                        Depends(injectTransitionLearningService)):
    print(f"controller -> predictWithTransitionLearning():"
          f"transitionLearningPredictRequestForm: {transitionLearningPredictRequestForm}")

    predictedNextSequence = transitionLearningService.predictText(transitionLearningPredictRequestForm)

    return JSONResponse(content=predictedNextSequence, status_code=status.HTTP_200_OK)

@transitionLearningRouter.post("/transition-learning-with-sentiment-analysis")
async def transitionLearningWithSentimentAnalysis(sentimentAnalysisRequestForm: SentimentAnalysisRequestForm,
                                                  transitionLearningService: TransitionLearningServiceImpl =
                                                  Depends(injectTransitionLearningService)):
    print(f"controller -> predictWithTransitionLearning():"
          f"transitionLearningPredictRequestForm: {sentimentAnalysisRequestForm}")

    predictedResult = transitionLearningService.transitionLearningWithSentimentAnalysis(sentimentAnalysisRequestForm)

    return JSONResponse(content=predictedResult, status_code=status.HTTP_200_OK)

@transitionLearningRouter.post("/gpt2-pretrained-prediction")
async def gpt2PretrainedPrediction(gpt2PretrainedPredictionRequestForm: GPT2PretrainedPredictionRequestForm,
                                   transitionLearningService: TransitionLearningServiceImpl =
                                   Depends(injectTransitionLearningService)):
    print(f"controller -> predictWithTransitionLearning():"
          f"transitionLearningPredictRequestForm: {gpt2PretrainedPredictionRequestForm}")

    predictedResult = transitionLearningService.predictTextWithGPT2(gpt2PretrainedPredictionRequestForm)

    return JSONResponse(content=predictedResult, status_code=status.HTTP_200_OK)