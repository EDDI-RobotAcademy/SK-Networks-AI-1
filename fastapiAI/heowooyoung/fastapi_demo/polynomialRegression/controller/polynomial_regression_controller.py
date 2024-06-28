from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from polynomialRegression.service.polynomial_regression_service_impl import PolynomialRegressionServiceImpl
from train_test_evaluation.controller.response_form.analysis_result_response_form import AnalysisResultResponseForm

polynomialRegressionRouter = APIRouter()

# Dependency Injection on Asynchronous Framework
# (비동기 프레임워크에서는 기존 동기 프레임워크와 다르게 싱글톤 방식으로 구성할 수 없음)

# 대표적으로 Spring과 Spring Reactive가 차이가 있음
# Spring과 결이 같은 녀석들이 Flask, Django 에 해당함
# Spring Reactive와 결이 같은 녀석은 FastAPI라고 보면 됨

# 둘의 가장 큰 차이는 Request 이후 Response 까지 Blocking이 발생하는지 안하는지 여부에 해당함
# 이전에 Multi-Tasking이나 Context Switching 이야기를 하면서
# Task들이 서로 자원(CPU, Memory, 기타 등등)을 획득하기 위해 전쟁을 치루는 것을 볼 수 있었음
# 가장 큰 문제점이라면 자원은 한정적인데 어떤 녀석이 Request 이후
# Response 가 완료 될 때까지 전체 자원을 혼자 다 독차지 하고 있다는 것이 문제가 되는 것임
# (왜냐하면 request가 한 두개가 아니라 여러 다발로 빈번하게 요청이 오기 때문) <- 대규모 서비스

# 사실 대규모 서비스가 아니라면 이러한 요소는 고려하지 않아도 됨 (일반적으로)
# 그러나 AI라는 분야에 한정하여 일반적인 상황에서도 이러한 고려가 필요해짐
# 왜냐하면 여러 사용자들이 접속할 때 위의 비동기, 동기 문제가 발생하면서 
# 모든 서버가 터지고 뻗는 대형 사고가 발생하기 때문임

# * Blocking
#   CPU 자원을 계속 붙잡고 놓지 않는 상황임

# * Non-Blocking
#   Blocking과는 조금 다른데 예로 한순간에 1000개가 들어오지만
#   3시간 동안 아무런 입력이 없는 경우가 있을 수 있음
#   보편적으로 Polling 방식을 이용해서 Blocking을 하면 
#   매 순간 "이거 있어 ?", "저거 했어 ?", "지금 어디까지 했어요 ?", "지금 뭐하고 있나요 ?" 같은 것을 묻는 것임
#   Non-Blocking 방식은 "나 이거 했다, 여유 되면 가져가"
#   조금 정신 없다가 나중에 확인하고 "어 가져갈게, 나는 요거 했어, 필요하면 가져가"
#   또 다른 녀석들이 와서 "ㅇㅋ 확인함, 난 요거 했고 저거 해어 가져가"
#   위와 같은 형태로 쪼는 형태가 아닌 구성을 가지게 됨
#   실제로 재밌는 것은 Blocking 방식은 단순 작업에서 효율이 높지만
#   복잡한 작업에서 Blocking은 오히려 성능을 대폭 하락시키고 서비스가 터지는 사고를 유발하게 됨
#   이유는 Request를 요청하고 응답하기까지 시간이 오래 걸리면
#   다른 서버들의 요청에 대한 응답 처리를 하지 못하고 Timeout 뜨면서 모든 것이 터지는 상황이 발생함
#   axios에 Timeout을 2500(2.5초) 굉장히 길게 줬는데 Blocking 하면 2.5초는 우습게 씹어먹고 다 터짐

# 고로 Event Driven 방식을 사용해서 Non-Blocking 방식으로
# "야 나 지금 이거 했어, 필요하면 가져가" 하고 다른 것을 대기하지 않고 바로 다음 작업에 착수하게 됨
# 사실 지금 우리가 사용하고 있는 애자일 보드나, 이슈 시스템, 슬랙 묶어 놓은 것도 이 방식이긴함
# FastAPI나 Spring Reactive는 이러한 것들을 서포트한다 보면 되겠음
# 고로 FastAPI에서 서포트하는 Depends를 사용하여 의존성을 엮으면 이런 문제들을 알아서 해결해준다 보면 됨
# 물론 여기서 조금 더 엮으려면 Apache Kafka 같은 것도 필요함

# 간략하게 기억할 점
# Django, Flask: Request 이후 Response 까지 무한정 대기해야함
# FastAPI: Request 받으면 내부에서 처리하는 Thread Pool들이 다 쪼개서 작업을 가져감
#          작업 전체는 보장을 위해 A 처리를 여러명이서 하지 않고
#          Request 이후 처리 작업들(AA, BB, CC)이 있다면
#          AA, BB, CC를 모두 다른 Thread가 처리한다 보면 되겠음
#          결국 여기다가는 Blocking 함수를 쓰면 재앙이 발생하게 됨

# AI 처리하는 상황에서 보자면 AI 처리해줘 -> 하고 대기하지 않음
# 처리 요청한거 잘 받았어 응답
# 다 처리하고 "야 이거 처리 했으니까 받어"

async def injectPolynomialRegressionService() -> PolynomialRegressionServiceImpl:
    return PolynomialRegressionServiceImpl()


@polynomialRegressionRouter.get("/polynomial-regression",)
async def polynomialRegression(polynomialRegressionService: PolynomialRegressionServiceImpl =
                               Depends(injectPolynomialRegressionService)):
    X, y, X_new, y_pred = await polynomialRegressionService.createSampleForPolynomialRegression()

    return {
        "X": X,
        "y": y,
        "X_new": X_new,
        "y_pred": y_pred,
    }
