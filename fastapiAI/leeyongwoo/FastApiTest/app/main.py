import os

import aiomysql
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from async_db.database import getMySqlPool, createTableIfNeccessary
from decision_tree.controller.decision_tree_controller import decisionTreeRouter
from exponential_regression.controller.exponential_regression_controller import exponentialRegressionRouter
from gradient_descent.controller.gradient_descent_controller import gradientDescentRouter
from kmeans.controller.kmeans_controller import kmeansRouter
from logistic_regression.controller.logistic_regression_controller import logisticRegressionRouter
from orders_analysis.controller.orders_analysis_controller import ordersAnalysisRouter
from polynomialRegression.controller.polynomial_regression_controller import polynomialRegressionRouter
from post.controller.post_controller import postRouter
from random_forest.controller.random_forest_controller import randomForestRouter
from tf_iris.controller.tf_iris_controller import tfIrisRouter
from train_test_evaluation.controller.train_test_evaluation_controller import trainTestEvaluationRouter

# # 현재는 deprecated 라고 나타나지만 lifespan 이란 것을 대신 사용하라고 나타나고 있음
# # 완전히 배제되지는 않았는데 애플리케이션이 시작할 때 실행될 함수를 지정함
# # 고로 애플리케이션 시작 시 비동기 처리가 가능한 DB를 구성한다 보면 됨
# @app.on_event("startup")
# async def startup_event():
#     app.state.db_pool = await getMySqlPool()
#     await createTableIfNeccessary(app.state.db_pool)
#
#
# # 위의 것이 킬 때 였으니 이건 반대라 보면 됨
# @app.on_event("shutdown")
# async def shutdown_event():
#     app.state.db_pool.close()
#     await app.state.db_pool.wait_closed()

import warnings

warnings.filterwarnings("ignore", category=aiomysql.Warning)

async def lifespan(app: FastAPI):
    # Startup
    app.state.dbPool = await getMySqlPool()
    await createTableIfNeccessary(app.state.dbPool)

    yield

    # Shutdown
    app.state.dbPool.close()
    await app.state.dbPool.wait_closed()


app = FastAPI(lifespan=lifespan)

# 웹 브라우저 상에서 "/" 을 입력하면 (key)Hello: (value)World가 리턴
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 브라우저 상에 /items/4?q=test 같은 것을 넣으면
# item_id로 4, q로는 "test"를 획득하게 됨
# 브라우저 상에서 get은 파라미터를 '?' 로 구분함
# 즉 위의 형식은 q 변수에 test를 넣겠단 소리
# 또한 vue에서의 가변 인자와는 조금 다르게
# 여기서 가변 인자는 아래와 같이 {item_id} 로 중괄호로 감쌈
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 사실 현재 위의 코드는 매우 근본이 없는 .... 코드임
# 왜냐하면 모든 로직을 main에 전부 따 때려박았기 때문
# 실질적으로 router(controller) 역할을 하는 녀석들을 분리할 필요가 있음
# 이것도 최소한이고 REST API 특성상
# service, repository, controller가 동일하게 필요함
# 그러나 우선 요번 케이스에서는 controller만 구성하도록 함
# 추가적으로 Vue + Django 상황에서는 이야기 하지 않았지만
# DTO (request_form, request, response, response_form)도 필요함
# DTO라는 용어조차 사실 다소 근본없다 생각하므로
# 우리의 경우엔 request_form, request,
# response, response_form 으로 구성할 것임

# DTO라는 용어가 근본이 없다 생각하는 이유는
# 나중에 현업 수준으로 구성이 커지게 되면 request도 엄청나게 많아지고
# response도 엄청난 분량으로 늘어나게됨
# 그럼 잠깐 머뭇하면서 이게 요청인가 응답인가 고민하면서 집중이 깨짐
# 아마 우리 프로젝트 하면서도
# 엄청나게 비대해지는 것을 볼 수 있을 것이라 생각됨

# 그럼 갑자기 궁금한 것이 생김
# request와 request_form의 차이는 뭔가 ?
# response와 response_form의 차이는 ?
# 둘 다 일맥상통한데 controller 쪽을 왔다갔다 하는 녀석들은 form이 붙음
# service 쪽에서는 request, response로 사용한다 보면 됨
# 결국 Full DDD를 할 때는 필요한 것임

# 요약하자면 form 이 붙으면 controller <-> service
# form이 없으면 service <-> entity
# 그래서 내부 객체에 toXXXRequest,
# fromXXXResponseForm 같은 형태가 만들어질 수 있음

# 초반에 이야기하지 않은 이유는 '일단 만들자' <<< 가 중요해서
# 만들어 놓고 이런 부분이 좀 '짜치는데 ?' 하면서
# 점진적으로 개선시키는 것이 '애자일' 방식임
# (빠른 습득 및 생산성의 비밀임 ㅇㅇ)

app.include_router(logisticRegressionRouter)
app.include_router(trainTestEvaluationRouter)
app.include_router(polynomialRegressionRouter)
app.include_router(exponentialRegressionRouter)
app.include_router(randomForestRouter)
app.include_router(postRouter, prefix="/post")
app.include_router(kmeansRouter)
app.include_router(tfIrisRouter)
app.include_router(ordersAnalysisRouter)
app.include_router(gradientDescentRouter)
app.include_router(decisionTreeRouter)

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
    uvicorn.run(app, host="192.168.0.9", port=33333)