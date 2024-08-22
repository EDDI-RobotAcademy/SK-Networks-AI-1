import json
import os
import asyncio

import aiomysql
import nltk
from aiokafka.admin import AIOKafkaAdminClient, NewTopic
from aiokafka.errors import TopicAlreadyExistsError
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from pydantic import BaseModel

from async_db.database import getMySqlPool, createTableIfNeccessary
from convolution_neural_network.controller.cnn_controller import convolutionNeuralNetworkRouter
# from decision_tree.controller.decision_tree_controller import decisionTreeRouter
from exponential_regression.controller.exponential_regression_controller import exponentialRegressionRouter
from gradient_descent.controller.gradient_descent_controller import gradientDescentRouter
from kmeans.controller.kmeans_controller import kmeansRouter
from language_model.controller.language_model_controller import languageModelRouter
from logistic_regression.controller.logistic_regression_controller import logisticRegressionRouter
from openai_basic.controller.openai_basic_controller import openAIBasicRouter
from orders_analysis.controller.orders_analysis_controller import ordersAnalysisRouter
from polynomialRegrssion.controller.polynomial_regression_controller import polynomialRegressionRouter
from post.controller.post_controller import postRouter
from principal_component_analysis.controller.pca_controller import principalComponentAnalysisRouter

from random_forest.controller.random_forest_controller import randomForestRouter
from recurrent_neural_network.controller.rnn_controller import recurrentNeuralNetworkRouter
from review_analysis.controller.review_analysis_controller import reviewAnalysisRouter
from sentence_structure_analysis.controller.sentence_structure_analysis_controller import \
    sentenceStructureAnalysisRouter
from sentitest.controller.senticontrol import naturalLanguageProcessingRouter
from sequence_analysis.controller.sequence_analysis_controller import sequenceAnalysisRouter
from srbcb.controller.srbcb_controller import srbcbRouter
from tf_idf_bow.controller.tf_idf_bow_controller import tfIdfBowRouter
from tf_iris.controller.tf_iris_controller import tfIrisRouter
from train_test_evaluation.controller.train_test_evaluation_controller import trainTestEvaluationRouter
from transition_learning.controller.transition_learning_controller import transitionLearningRouter
from vector_db.database import getMongoDBPool


async def create_kafka_topics():
    adminClient = AIOKafkaAdminClient(
        bootstrap_servers='localhost:9092',
        loop=asyncio.get_running_loop()
    )

    try:
        await adminClient.start()

        topics = [
            NewTopic(
                "test-topic",
                num_partitions=1,
                replication_factor=1,
            ),
            NewTopic(
                "completion-topic",
                num_partitions=1,
                replication_factor=1,
            ),
        ]

        for topic in topics:
            try:
                await adminClient.create_topics([topic])
            except TopicAlreadyExistsError:
                print(f"Topic '{topic.name}' already exists, skipping creation")

    except Exception as e:
        print(f"카프카 토픽 생성 실패: {e}")
    finally:
        await adminClient.close()

# 프로그램 시작할 때와 꺼질 때
# 애플리케이션 시작 시 비동기 처리가 가능한 DB를 구성
# @app.on_event("startup")
# async def startup_event():
#     app.state.db_pool = await getMySqlPool()
#     await createTableIfNeccessary(app.state.db_pool)
#
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

    app.state.vectorDBPool = await getMongoDBPool()

    # # 비동기 I/O 정지 이벤트 감지
    # app.state.stop_event = asyncio.Event()
    #
    # # Kafka Producer (생산자) 구성
    # app.state.kafka_producer = AIOKafkaProducer(
    #     bootstrap_servers='localhost:9092',
    #     client_id='fastapi-kafka-producer'
    # )
    #
    # # Kafka Consumer (소비자) 구성
    # app.state.kafka_consumer = AIOKafkaConsumer(
    #     'completion_topic',
    #     bootstrap_servers='localhost:9092',
    #     group_id="my_group",
    #     client_id='fastapi-kafka-consumer'
    # )
    #
    # # 자동 생성했던 test-topic 관련 소비자
    # app.state.kafka_test_topic_consumer = AIOKafkaConsumer(
    #     'test-topic',
    #     bootstrap_servers='localhost:9092',
    #     group_id="another_group",
    #     client_id='fastapi-kafka-consumer'
    # )
    #
    # await app.state.kafka_producer.start()
    # await app.state.kafka_consumer.start()
    # await app.state.kafka_test_topic_consumer.start()
    #
    # # asyncio.create_task(consume(app))
    # asyncio.create_task(testTopicConsume(app))

    try:
        yield
    finally:
        # Shutdown
        app.state.dbPool.close()
        await app.state.dbPool.wait_closed()

        app.state.vectorDBPool.close()
        await app.state.vectorDBPool.wait_closed()

        # app.state.stop_event.set()
        #
        # await app.state.kafka_producer.stop()
        # await app.state.kafka_consumer.stop()
        # await app.state.kafka_test_topic_consumer.stop()

app = FastAPI(lifespan=lifespan)


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

def download_nltk_data():
    nltk_data_path = os.path.join(os.path.expanduser("~"), "nltk_data")
    if not os.path.exists(nltk_data_path):
        os.makedirs(nltk_data_path)

    if not os.path.exists(os.path.join(nltk_data_path, "corpora", "stopwords")):
        nltk.download('stopwords', download_dir=nltk_data_path)

    # punkt 다운로드
    if not os.path.exists(os.path.join(nltk_data_path, "tokenizers", "punkt")):
        nltk.download('punkt', download_dir=nltk_data_path)

download_nltk_data()

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
# app.include_router(decisionTreeRouter)
app.include_router(principalComponentAnalysisRouter)
app.include_router(convolutionNeuralNetworkRouter)
app.include_router(recurrentNeuralNetworkRouter)
app.include_router(sentenceStructureAnalysisRouter)
app.include_router(srbcbRouter)
app.include_router(tfIdfBowRouter)
app.include_router(sequenceAnalysisRouter)
app.include_router(languageModelRouter)
app.include_router(reviewAnalysisRouter)
app.include_router(naturalLanguageProcessingRouter)
app.include_router(transitionLearningRouter)
app.include_router(openAIBasicRouter)

async def testTopicConsume(app: FastAPI):
    consumer = app.state.kafka_test_topic_consumer

    while not app.state.stop_event.is_set():
        try:
            msg = await consumer.getone()
            data = json.loads(msg.value.decode("utf-8"))
            print(f"request data: {data}")

            # 실제로 여기서 뭔가 요청을 하던 뭘 하던 지지고 볶으면 됨
            await asyncio.sleep(60) # 1분 대기시간 걸어줌

            for connection in app.state.connections:
                await connection.send_json({
                    'message': 'Processing completed.',
                    'data': data,
                    'title': "Kafka Test"
                })

        except asyncio.CancelledError:
            print("소비자 태스크 종료")
            break

        except Exception as e:
            print(f"소비 중 에러 발생: {e}")


load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.state.connections = set()

class KafkaRequest(BaseModel):
    message: str

@app.post("/kafka-endpoint")
async def kafka_endpoint(request: KafkaRequest):
    eventData = request.dict()
    await app.state.kafka_producer.send_and_wait("test-topic", json.dumps(eventData).encode())

    return {"status" : "processing"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    app.state.connections.add(websocket)

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        app.state.connections.remove(websocket)

if __name__ == "__main__":
    import uvicorn
    # asyncio.run(create_kafka_topics())
    uvicorn.run(app, host="127.0.0.1", port=33333)