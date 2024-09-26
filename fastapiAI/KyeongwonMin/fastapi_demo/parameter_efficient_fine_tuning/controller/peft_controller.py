import os
import time

from fastapi import FastAPI, APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

peftFineTuningRouter = APIRouter()

training_data = [
    {"prompt": "Hello, how are you?", "completion": "I'm good, thank you!"},
    {"prompt": "What's your favorite color?", "completion": "My favorite color is blue."}
]

@peftFineTuningRouter.post("/peft-test")
def get_fine_tune_status():
    with open('fine_tune_data.jsonl', 'w') as f:
        for item in training_data:
            f.write(f'{{"prompt": "{item["prompt"]}", "completion": "{item["completion"]}"}}\n')

    file_path = "fine_tune_data.jsonl"
    with open(file_path, "rb") as f:
        response = openai.files.create(file=f, purpose='fine-tune')

    file_id = response.id

    # 모델 미세 조정 시작
    fine_tune_response = openai.fine_tuning.jobs.create(training_file=file_id, model="gpt-3.5-turbo-0613")

    # Fine-tune 진행 상태 확인
    while True:
        status = openai.fine_tuning.jobs.retrieve(fine_tune_response.id)
        status_code = status['status']
        if status_code in ["succeeded", "failed"]:
            print(f'Fine-tuning job status: {status_code}')
            break

        time.sleep(30)

    return {"response": status}
