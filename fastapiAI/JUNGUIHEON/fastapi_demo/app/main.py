import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from logistic_regression.controller.logistic_regression_controller import logisticRegressionRouter
from train_test_evaluation.controller.train_test_evaluation_controller import trainTestEvaluationRouter

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

app.include_router(logisticRegressionRouter)
app.include_router(trainTestEvaluationRouter)


load_dotenv()

origins = os.getenv('ALLOWED_ORIGINS', "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port= 33333)