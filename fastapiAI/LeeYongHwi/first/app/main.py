from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logistic_regression.controller.logistic_regression_controller import logisticRegressionRouter
import os

app = FastAPI()

# 웹 브라우저 상에서 "/"를 입력하면 (key)Hello: (value)World가 리턴
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 브라우저 상에 /items/4?q=test 같은 것을 넣으면
# item_id로 4, q로는 "test"를 획득하게 됨
# 브라우저 상에서 get은 파라미터를 '?'로 구분함
# 즉 위의 형식은 q 변수에 test를 넣겠단 소리
# 또한 vue에서의 가변 인자와는 조금 다르게
# 여기서 가변 인자는 아래와 같이 {item_id}로 중괄호로 감쌈
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 사실 현재 위의 코드는 매우 근본이 없는 코드임
# 왜냐하면 모든 로직을 main에 전부 넣었기 때문
# 실질적으로 router(controller) 역할을 하는 녀석들을 분리할 필요가 있음
# 이것도 최소한이고 REST API 특성상
# service, repository, controller가 동일하게 필요함
# 그러나 우선 요번 케이스에서는 controller만 구성하도록 함
# 추가적으로 Vue + Django 상황에서는 이야기 하지 않았지만
# DTO (request_form, request, response, response_form)도 필요함
# DTO라는 용어조차 사실 다소 근본이 없음
# 우리의 경우엔 request_form. request,
# response, response_form으로 구성할 것임

# DTO라는 용어가 근본이 없다 생각하는 이유는
# 나중에 현업 수준으로 구성이 커지게 되면 request도 엄청나게 많아지고
# response도 엄청난 분량으로 늘어나게 됨
# 그럼 잠깐 머뭇하면서 이게 요청인가 응답인가 고민하면서 집중이 깨짐
# 아마 우리 프로젝트 하면서도
# 엄청나게 비대해지는 것을 볼 수 있을 것이라 생각됨

# 그럼 갑자기 궁금한 것이 생김
# request와 request_form의 차이는 뭔가?
# response와 response_form의 차이는?
# 둘 다 일맥상통한데 controller 쪽을 왔다 갔다 하는 녀석들은 form이 붙음
# service 쪽에서는 request, response로 사용한다 보면 됨
# 결국 Full DDD를 할 때는 필요한 것임

# 요약하자면 form이 붙으면 controller <-> service
# form이 없으면 service <-> entity
# 그래서 내부 객체에 toXXXrequest,
# fromXXXResponseForm 같은 형태가 만들어질 수 있음

# 초반에 이야기하지 않은 이유는 '일단 만들자' <<< 가 중요해서
# 만들어 놓고 이런 분이 좀 별론데? 하면서
# 점진적으로 개선시키는 것이 '애자일' 방식임

app.include_router(logisticRegressionRouter)

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=33333)