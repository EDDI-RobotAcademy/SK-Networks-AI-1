import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logistic_regression.controller.logistic_regression_controller import logisticRegressionRouter
from train_test_evaluation.controller.train_test_evaluation_controller import trainTestEvaluationRouter
from polynomialRegression.controller.polynomial_regression_controller import polynomialRegressionRouter
app = FastAPI()

# 웹 브라우저 상에서 "/" 를 입력하면 Hello World가 리턴
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 브라우저 상에 "/items/4&q="test" 같은 것을 넣으면
# item_id로 4, q로는 "test"를 획득하게 됨
# 브라우저 상에서 get은 파라미터를 '?'로 구분함
# 즉 위의 형식은 q 변수에 test를 넣겠다는 소리
# 또한 Vue에서의 가변 인자와는 조금 다르게
# 여기서 가변 인자는 아래와 같이 {item_id}로 중괄호로 감싼다.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Vue와 fastapi 통신을 위함
# app은 django에서의 main.urls.py 기능을 함
# router = urls (통신을 위함)
app.include_router(logisticRegressionRouter)
app.include_router(trainTestEvaluationRouter)
app.include_router(polynomialRegressionRouter)

# env 관련 설정
# 통신하는 과정에서 우리가 허락한 것만 받아 들이겠다.
load_dotenv()
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
# 어떤 애들을 CORS 정책에 허용할지 정함
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=33333) # Django랑 충돌하는거 강제로 맞추기 (되도록 33333 으로..)
