import asyncio
import os
import json

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

import aiomysql
from aiokafka.admin import AIOKafkaAdminClient, NewTopic
from aiokafka.errors import TopicAlreadyExistsError
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocketDisconnect, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from async_db.database import getMySqlPool, createTableIfNeccessary
from convolution_neural_network.controller.cnn_controller import ConvolutionNeuralNetworkRouter
# from decision_tree.controller.decision_tree_controller import decisionTreeRouter # .so 파일 이슈
from exponential_regression.controller.exponential_regression_controller import exponentialRegressionRouter
from gradient_descent.controller.gradient_descent_controller import gradientDescentRouter
# from kmeans.controller.kmeans_controller import kmeansRouter
from logistic_regression.controller.logistic_regression_controller import logisticRegressionRouter
from orders_analysis.controller.orders_analysis_controller import OrdersAnalysisRouter
from polynomialRegression.controller.polynomial_regression_controller import polynomialRegressionRouter
from post.controller.post_controller import postRouter
from principal_component_analysis.controller.pca_controller import PrincipalComponentAnalysisRouter
from random_forest.controller.random_forest_controller import randomForestRouter
from recurrent_neural_network.controller.rnn_controller import recurrentNeuralNetworkRouter
from tf_iris.controller.tf_iris_controller import tfIrisRouter
from train_test_evaluation.controller.train_test_evaluation_controller import trainTestEvaluationRouter

import warnings
# aiomysql 관련 warning 메세지 무시
warnings.filterwarnings("ignore", category=aiomysql.Warning)

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

# topic 다루는 함수
async def create_kafka_topics():
    # adminClient 해줌으로써 mysql 처럼 kafka 접근가능하게 해줌
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
                print(f"Topic '{topic.name}' already exists, skippint creation")
    except Exception as e:
        print(f"카프카 토픽 생성 실패: {e}")
    finally:
        await adminClient.close()

async def lifespan(app: FastAPI):
    # Startup
    app.state.dbPool = await getMySqlPool()
    await createTableIfNeccessary(app.state.dbPool)

    # 비동기 I/O 정지 이벤트 감지 (학습,추론 중이라 다른 일 못할때 이 부분이 지원)
    # import asyncio
    app.state.stop_event = asyncio.Event()

    # Kafka Producer (생산자) 구성
    # from aiokafka import AIOKafkaProducer
    app.state.kafka_producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092',
        client_id='fastapi-kafka-producer'
    )

    # Kafka Consumer (소비자) 구성
    # from aiokafka import AIOKafkaConsumer
    app.state.kafka_consumer = AIOKafkaConsumer(
        'completion_topic',
        bootstrap_servers='localhost:9092',
        group_id='my_group',
        client_id='fastapi-kafka-consumer'
    )

    # 자동 생성했던 test-topic 관련 소비자
    app.state.kafka_test_topic_consumer = AIOKafkaConsumer(
        'test-topic',
        bootstrap_servers='localhost:9092',
        group_id='another_group',
        client_id='fastapi-kafka-consumer'
    )

    # 각각의 thread start
    await app.state.kafka_producer.start()
    await app.state.kafka_consumer.start()
    await app.state.kafka_test_topic_consumer.start()

    #asyncio.create_task(consume(app))
    asyncio.create_task(testTopicConsume(app))

    try:
        yield
    finally:
        # 기존 db pool shut down 기능도 여기에 두기
        # Shutdown
        app.state.dbPool.close()
        await app.state.dbPool.wait_closed()

        app.state.stop_event.set()

        # kafka 종료
        await app.state.kafka_producer.stop()
        await app.state.kafka_consumer.stop()
        await app.state.kafka_test_topic_consumer.stop()



app = FastAPI(lifespan=lifespan)

# 웹 브라우저 상에서 "/" 을 입력하면 (key)Hello: (value)World가 리턴
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

async def testTopicConsume(app: FastAPI):
    consumer = app.state.kafka_test_topic_consumer

    while not app.state.stop_event.is_set():
        try:
            msg = await consumer.getone()
            data = json.loads(msg.value.decode('utf-8'))
            print(f"request data: {data}")

            # 여기서 부터 소비자가 무엇을 할건지 작성하면 됨
            await asyncio.sleep(60) # 1분 대기

            # 이것과 연결된 모든 사용자들은 해당 메세지를 받음
            for connection in app.state.connections:
                await connection.send_json({
                    'message':'Processing completed.',
                    'data':data,
                    'title':"Kafka Test"
                })

        except asyncio.CancelledError:
            print("소비자 태스크 종료")
            break

        except Exception as e:
            print(f"소비 중 에러 발생: {e}")


app.include_router(logisticRegressionRouter)
app.include_router(trainTestEvaluationRouter)
app.include_router(polynomialRegressionRouter)
app.include_router(exponentialRegressionRouter)
app.include_router(randomForestRouter)
app.include_router(postRouter, prefix="/post")
# app.include_router(kmeansRouter)
app.include_router(tfIrisRouter)
app.include_router(OrdersAnalysisRouter)
app.include_router(gradientDescentRouter)
# app.include_router(decisionTreeRouter)
app.include_router(PrincipalComponentAnalysisRouter)
app.include_router(ConvolutionNeuralNetworkRouter)
app.include_router(recurrentNeuralNetworkRouter)
load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.connections = set()

class KafkaRequest(BaseModel):
    message: str
@app.post("/kafka-endpoint")
async def kafka_endpoint(request: KafkaRequest):
    eventData = request.dict()
    await app.state.kafka_producer.send_and_wait("test-topic", json.dumps(eventData).encode())

    return {"status":"processing"}

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
    asyncio.run(create_kafka_topics())
    uvicorn.run(app, host="192.168.0.44", port=33333) # localhost -> 자기 ipv4 주소로 변경