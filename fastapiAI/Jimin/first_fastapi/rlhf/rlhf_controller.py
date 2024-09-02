import json
import os

import openai
from dotenv import load_dotenv
from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable")

# Reinforcement Learning from Human Feedback
rlhfFineTuningRouter = APIRouter()

# 피드백 데이터 저장
feedbackData = []

# 이전 파인 튜닝 데이터 그대로 가져오면 됩니다
trainingData = [
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "광역기는 배틀 필드에 나와 있는 모든 유닛을 공격 할 수 있습니다."},
        {"role": "assistant", "content": "모든 유닛을 공격합니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "단일기는 배틀 필드에 있는 특정 유닛을 공격 할 수 있습니다."},
        {"role": "assistant", "content": "특정 유닛을 공격합니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "네더 블레이드는 매턴 광역기와 단일기를 사용합니다."},
        {"role": "assistant", "content": "네더 블레이드는 매턴 광역기와 단일기를 사용합니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "네더 블레이드의 광역기는 10의 피해를 줍니다."},
        {"role": "assistant", "content": "네더 블레이드의 광역기는 10의 피해를 줍니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "네더 블레이드의 단일기는 20의 피해를 줍니다."},
        {"role": "assistant", "content": "네더 블레이드의 단일기는 20의 피해를 줍니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "모든 유닛은 HP와 ATK(공격력)을 가지고 있다."},
        {"role": "assistant", "content": "모든 유닛은 HP와 ATK를 가지고 있습니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "특수 효과가 붙어 있지 않는 한 HP가 0이 되면 유닛은 무덤으로 이동한다."},
        {"role": "assistant", "content": "HP가 0이 되면 유닛은 무덤으로 이동합니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "광역기는 모든 적 유닛에게 피해를 줍니다.."},
        {"role": "assistant", "content": "광역기는 모든 적 유닛에게 피해를 줍니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "단일기는 하나의 적 유닛에게 큰 피해를 줍니다."},
        {"role": "assistant", "content": "단일기는 하나의 적 유닛에게 큰 피해를 줍니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "아이템 카드 중 일부는 유닛을 공격 할 수 있습니다."},
        {"role": "assistant", "content": "일부 아이템 카드는 유닛을 공격할 수 있습니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "네더 블레이드가 광역기로 줄 수 있는 데미지가 얼마야?"},
        {"role": "assistant", "content": "네더 블레이드의 광역기로 줄 수 있는 데미지는 10입니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "네더 블레이드의 광역기 데미지가 몇인가요?"},
        {"role": "assistant", "content": "네더 블레이드의 광역기로 줄 수 있는 데미지는 10입니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "네더 블레이드의 광역기는 몇 데미지를 주나요?"},
        {"role": "assistant", "content": "네더 블레이드의 광역기로 줄 수 있는 데미지는 10입니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "유닛의 HP가 30일 때, 네더 블레이드가 1턴에 이 유닛을 정리 할 수 있나요?"},
        {"role": "assistant", "content": "네, 네더 블레이드는 1턴에 유닛을 정리 할 수 있습니다." 
                                         "네더 블레이드의 광역기는 10의 피해를 주고, 단일기는 20의 피해를 줍니다. 따라서 총 30의 피해를 줄 수 있습니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "유닛의 HP가 50일 때, 네더 블레이드가 1턴에 이 유닛을 정리 할 수 있나요?"},
        {"role": "assistant", "content": "아니요, 네더 블레이드는 1턴에 유닛을 정리 할 수 없습니다." 
                                         "네더 블레이드의 광역기는 10의 피해를 주고, 단일기는 20의 피해를 줍니다. 따라서 총 30의 피해를 줄 수 있습니다."}
    ]},
]

class Feedback(BaseModel):
    fineTuneId: str
    prompt: str
    response: str
    feedback: str # 'positive' 또는 'negative'
    betterResponse: str = None

# 피드백을 수집하는 엔드포인트
@rlhfFineTuningRouter.post("/give-feedback")
def giveFeedback(feedback: Feedback):
    feedbackData.append(feedback.dict())
    return {"status": "Feedback received"}

# 피드백을 처리하여 새로운 훈련 데이터를 생성하는 함수
def processFeedback():
    trainingData = []
    for item in feedbackData:
        if item['feedback'] == 'negaitve':
            # 부정적인 피드백에 대한 개선된 응답을 수집
            betterResponse = item.get('betterResponse')
            if not betterResponse:
                betterResponse = f"이것은 잘못된 답변입니다.: {item.get('response')}"

            newTrainingExample = {
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "system", "content": item['prompt']},
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
    saveTrainingData(trainingData)

    filePath = "training_data.jsonl"
    with open(filePath, "rb") as file:
        response = openai.files.create(file=file, purpose='fine-tune')

        fileId = response.id
        fineTuneResponse = openai.fine_tuning.jobs.create(
            training_file=fileId,
            model="gpt-3.5-turbo-0613",
            hyperparameters={
                "n_epochs": 10
            }
        )
        return fineTuneResponse.id


# 파인 튜닝을 피드백 기반으로 시작하는 엔드포인트
@rlhfFineTuningRouter.post("/fine-tune-with-feedback")
def fineTuneWithFeedback(backgroundTasks: BackgroundTasks):
    processFeedback() # 피드백을 처리하여 새로운 훈련 데이터를 생성
    fineTuneId = startFineTuning() # 새로운 데이터로 모델을 미세 조정
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

class Query(BaseModel):
    text: str

@rlhfFineTuningRouter.post("/chat")
def chat_with_model(query: Query):
    fine_tuned_model = "ft:gpt-3.5-turbo-0613:jimin::A1OXUQka"
    response = openai.chat.completions.create(
        model=fine_tuned_model,
        messages=[{"role": "user", "content": query.text}]
    )
    return {"response": response.choices[0].message.content}