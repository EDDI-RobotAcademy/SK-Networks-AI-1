import os
import json
import openai
from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

rlhfFineTuningRouter = APIRouter()

# 피드백 데이터 저장
feedbackData = []


class Feedback(BaseModel):
    fineTuneId: str
    prompt: str
    response: str
    feedback: str  # 'positive' 또는 'negative'


# 피드백을 수집하는 엔드포인트
@rlhfFineTuningRouter.post("/give-feedback")
def giveFeedback(feedback: Feedback):
    feedbackData.append(feedback.dict())
    return {"status": "Feedback received"}


# 피드백을 처리하여 새로운 훈련 데이터를 생성하는 함수
def processFeedback():
    trainingData = []
    for item in feedbackData:
        if item['feedback'] == 'negative':
            # 부정적인 피드백에 대한 개선된 응답을 수집
            betterResponse = input(f"How would you improve the response for the prompt: '{item['prompt']}'?")
            newTrainingExample = {
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": item['prompt']},
                    {"role": "assistant", "content": betterResponse}
                ]
            }
            trainingData.append(newTrainingExample)

    # 생성된 훈련 데이터를 파일로 저장
    if trainingData:
        saveTrainingData(trainingData)


# 새로운 훈련 데이터를 저장하는 함수
def saveTrainingData(trainingData, filename="training_data.jsonl"):
    with open(filename, "w") as file:
        for item in trainingData:
            file.write(json.dumps(item) + "\n")


# 파인 튜닝을 시작하는 함수
def startFineTuning():
    filePath = "training_data.jsonl"
    with open(filePath, "rb") as file:
        response = openai.files.create(file=file, purpose='fine-tune')

    fileId = response.id
    fineTuneResponse = openai.fine_tuning.jobs.create(
        training_file=fileId,
        model="gpt-3.5-turbo-0613"
    )
    return fineTuneResponse.id


# 파인 튜닝을 피드백 기반으로 시작하는 엔드포인트
@rlhfFineTuningRouter.post("/fine-tune-with-feedback")
def fineTuneWithFeedback(backgroundTasks: BackgroundTasks):
    processFeedback()  # 피드백을 처리하여 새로운 훈련 데이터를 생성
    fineTuneId = startFineTuning()  # 새로운 데이터로 모델을 미세 조정
    backgroundTasks.add_task(checkFineTuneStatus, fineTuneId)
    return {"status": "Fine-tuning started with feedback", "fineTuneId": fineTuneId}


# 파인 튜닝 상태를 확인하는 함수
def checkFineTuneStatus(fineTuneId):
    statusResponse = openai.fine_tuning.jobs.retrieve(fineTuneId)
    status = statusResponse.status
    print(f"Fine-tuning status for {fineTuneId}: {status}")


# 파인 튜닝 상태를 확인하는 엔드포인트
@rlhfFineTuningRouter.get("/fine-tune-status/{fineTuneId}")
def getFineTuneStatus(fineTuneId: str):
    statusResponse = openai.fine_tuning.jobs.retrieve(fineTuneId)
    return {"status_response": statusResponse}
