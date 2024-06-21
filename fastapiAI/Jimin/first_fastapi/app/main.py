import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from exponenetial_regression.controller.exponential_regression_controller import exponentialRegressionRouter
from logistic_regression.controller.logistic_regression_controller import logisticRegressionRouter
from polynomialRegrssion.controller.polynomial_regression_controller import polynomialRegressionRouter
from random_forest.controller.random_forest_controller import randomForestRouter
from train_test_evaluation.controller.train_test_evaluation_controller import trainTestEvaluationRouter

app = FastAPI()

# 웹 브라우저 상에서 "/"을 입력하면 (key)Hello: (value)World가 리턴
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 웹 브라우저 상에 /items/4?q=test 같은 것을 넣으면
# item_id로 4, q로는 "test"를 획득하게 됨
# 브라우저 상에서 get은 파리미터를 '?'로 구분함
# 즉 위의 형식은 q 변수에 test를 넣겠단 소리
# 또한 vue에서의 가변 인자와는 조금 다르게
# 여기서 가변 인자는 아래와 같이 {item_id}로 중괄호로 감쌈
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 사실 현재 위의 코드는 매우 근본이 없는 코드
# 모든 로직을 main에 다 때려박았기 때문
# 실질적으로 router(controller) 역할을 하는 녀석들을 분리 할 필요가 있음
# REST API 특성상 service, repository, controller가 동일하게 필요함
# DTO (request_form, request, response, response_form)도 필요함
# controller쪽 왔다갔다 하는 녀석들은 form이 붙음
# service 쪽에서는 request, response로 사용한다 보면 됨
# form이 붙으면 controller <-> service
# 없으면 service <-> entity
# 따라서 내부 객체에 toXXXRequest, fromXXXResponsForm 같은 형태가 만들어질 수 있음

app.include_router(logisticRegressionRouter)
app.include_router(trainTestEvaluationRouter)
app.include_router(polynomialRegressionRouter)
app.include_router(exponentialRegressionRouter)
app.include_router(randomForestRouter)

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=33333)