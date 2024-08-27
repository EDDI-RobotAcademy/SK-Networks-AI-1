import json
import os

import openai
from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI, BackgroundTasks
from pydantic import BaseModel

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable")

app = FastAPI()

openAIFineTuningTestRouter = APIRouter()

training_data = [
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "광역기는 배틀 필드에 나와 있는 모든 유닛을 공격 할 수 있습니다"},
        {"role": "assistant", "content": "모든 유닛을 공격합니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "단일기는 배틀 필드에 있는 특정 유닛을 공격 할 수 있습니다."},
        {"role": "assistant", "content": "특정 유닛을 공격합니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "네더 블레이드는 매턴 광역기와 단일기를 사용합니다"},
        {"role": "assistant", "content": "네더 블레이드는 매턴 광역기와 단일기를 사용합니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "네더 블레이드의 광역기는 10의 피해를 줍니다"},
        {"role": "assistant", "content": "네더 블레이드의 광역기는 10의 피해를 줍니다"}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "네더 블레이드의 단일기는 20의 피해를 줍니다"},
        {"role": "assistant", "content": "네더 블레이드의 단일기는 20의 피해를 줍니다"}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "모든 유닛은 HP와 ATK(공격력)을 가지고 있다."},
        {"role": "assistant", "content": "모든 유닛은 HP와 ATK를 가지고 있습니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "특수 효과가 붙어 있지 않는 한 HP가 0이 되면 유닛은 무덤으로 이동한다"},
        {"role": "assistant", "content": "HP가 0이 되면 유닛은 무덤으로 이동합니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "광역기는 모든 적 유닛에게 피해를 줍니다"},
        {"role": "assistant", "content": "광역기는 모든 적 유닛에게 피해를 줍니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "단일기는 하나의 적 유닛에게 큰 피해를 줍니다"},
        {"role": "assistant", "content": "단일기는 하나의 적 유닛에게 큰 피해를 줍니다"}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "아이템 카드 중 일부는 유닛을 공격 할 수 있습니다"},
        {"role": "assistant", "content": "일부 아이템 카드는 유닛을 공격할 수 있습니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "네더 블레이드가 광역기로 줄 수 있는 데미지가 얼마야?"},
        {"role": "assistant", "content": "네더 블레이드의 광역기로 줄 수 있는 데미지는 10입니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "네더 블레이드의 광역기 데미지가 몇인가요?"},
        {"role": "assistant", "content": "네더 블레이드의 광역기로 줄 수 있는 데미지는 10입니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "유닛의 HP가 30일 때, 네더 블레이드가 1턴에 이 유닛을 정리할 수 있나요?"},
        {"role": "assistant",
         "content": "네, 네더 블레이드는 1턴에 유닛을 정리할 수 있습니다""네더 블레이드의 광역기는 10의 피해를 주고, 단일기는 20의 피해를 줍니다. 따라서 총 30의 피해를 줄 수 있습니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "유닛의 HP가 50일 때, 네더 블레이드가 1턴에 이 유닛을 정리할 수 있나요?"},
        {"role": "assistant",
         "content": "아니요, 네더 블레이드는 1턴에 유닛을 정리할 수 없습니다.""네더 블레이드의 광역기는 10의 피해를 주고, 단일기는 20의 피해를 줍니다. 따라서 총 30의 피해를 줄 수 있습니다."}
    ]},
    {"messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "네더 블레이드의 광역기는 몇 데미지를 주나요?"},
        {"role": "assistant", "content": "네더 블레이드의 광역기로 줄 수 있는 데미지는 10입니다.."}
    ]},
]


class Query(BaseModel):
    text: str


def save_model_trainingData(training_data, filename="training_data.jsonl"):
    with open(filename, "w") as f:
        for item in training_data:
            f.write(json.dumps(item) + "\n")


def start_fine_tuning():
    save_model_trainingData(training_data)

    file_path = ("training_data.jsonl")
    with open(file_path, "rb") as f:
        response = openai.files.create(file=f, purpose='fine-tune')

    print(f"File upload response: {response}")

    file_id = response.id
    fine_tune_response = openai.fine_tuning.jobs.create(training_file=file_id, model="gpt-3.5-turbo-0613")
    print(f"Fine-tuning started with ID: {fine_tune_response}")
    return fine_tune_response.id


@openAIFineTuningTestRouter.post("/fine-tune")
def fine_tune_model(background_tasks: BackgroundTasks):
    fine_tune_id = start_fine_tuning()
    background_tasks.add_task(check_fine_tune_status, fine_tune_id)
    return {"status": "Fine-tuning started", "fine_tune_id": fine_tune_id}


def check_fine_tune_status(fine_tune_id):
    status_response = openai.fine_tuning.jobs.retrieve(fine_tune_id)
    status = status_response.status
    print(f"Fine-tuning status for {fine_tune_id}: {status}")


@openAIFineTuningTestRouter.get("/fine-tune-status/{fine_tune_id}")
def get_fine_tune_status(fine_tune_id: str):
    status_response = openai.fine_tuning.jobs.retrieve(fine_tune_id)
    return {"status_response": status_response}


@openAIFineTuningTestRouter.post("/chat")
def chat_with_model(query: Query):
    fine_tune_model = "ft:gpt-3.5-turbo-0613:personal::A0KtpdqG"
    response = openai.chat.completions.create(model=fine_tune_model, messages=[{"role": "user", "content": query.text}])
    return {"response": response.choices[0].message.content}
