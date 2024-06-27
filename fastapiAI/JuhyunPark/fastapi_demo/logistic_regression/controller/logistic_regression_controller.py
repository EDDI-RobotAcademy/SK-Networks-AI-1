from fastapi import APIRouter
from fastapi.responses import JSONResponse

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 아래와 같이 APIRouter를 가져오면
# 생성한 router 이름으로 get, post 등등의 router를 구성할 수 있음
logisticRegressionRouter = APIRouter()

# @GetMapping
# @RequestMapping(get)
@logisticRegressionRouter.get("/logistic-regression")
def logistic_regression_test():
    print("logistic_regression_test()")

    np.random.seed(0)
    # 임의의 (x, y) 2차원 벡터(좌표)를 100개 생성
    X = np.random.randn(100, 2)
    # x 좌표와 y 좌표를 더해서 0 보다 크면 1, 아니면 0
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    # 자동으로 100개 중 30% 를 테스트 셋으로 지정함
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    print('X:', X)
    print('y:', y)
    
    # 학습 모델로 Logistic Regression을 선택
    model = LogisticRegression()
    # 테스트 외의 훈련 데이터를 가지고 실제 회귀 분석 진행
    model.fit(X_train, y_train)
    # 회귀 분석이란 ?
    # 결론적으로 Y = A.X + B 를 찾는 수학적인 기법이라 볼 수 있음
    # 기본적으로 증명을 위해선 편미분을 사용해야하나 ... 여기는 수학 학원이 아니니 배제 ㄷㄷㄷ
    # 기본적인 접근은 x 값에 대해 최소 오차가 얼마인지, y 값에 대한 최소 오차가 얼마인지를 판별하기 위해
    # 특정 방향 도함수(편미분)을 사용해야하는 것임
    # 미분하니 사실 좀 어질어질 할 수 있는데 복잡하게 생각할 필요 없이 미분은 변화율이라 생각하면 됨
    # 그러니 변화가 얼마나 적게 일어나는가를 기준으로
    # 함수를 어떻게 만들 것인가 추적하는 기법으로 정리할 수 있음

    # 그래프 추이를 보고 싶다면 https://www.wolframalpha.com/
    # 여기서 그냥 함수 형태를 입력하면 알아서 그려줌
    # ex) e^(-x^2) 을 표현해봅시다
    # https://www.wolframalpha.com/input?i=y+%3D+e%5E%28-x%5E2%29
    # 정규 분포를 그리는 것을 볼 수 있음
    # 결론적으로 회귀 분석에 여러 종류가 있는 이유는 여러 다양한 형태의 그래프를 표현하기 위해서임
    # 그리고 그 판단은 어쩔 수 없이 사람이 결정해줘야함
    # 무엇이 이 데이터에 더 적합한지
    
    # 테스트용 좌표를 가지고 결과값을 추론
    # X = [(1, 2), (3, 4), (2, 3), ... ]
    # y = [   1  ,    1  ,   1   , ... ]   
    y_pred = model.predict(X_test)
    
    # 예측치인 pred 값과 실제 테스트 셋인 test를
    # 비교하여 정확도가 어느정도인지 판별
    accuracy = accuracy_score(y_test, y_pred)
    # y = ax + b 라 가정 했을 때 coef_ 는 a를 의미함
    coef = model.coef_
    # y = ax + b에서 intercept_ 는 b를 의미함
    intercept = model.intercept_

    # x 값을 일정 범위로 설정!
    # 100개의 x 성분 중 최소값과 최대값을 뽑아서 일정 간격으로 분할
    x_values = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
    # 어떤 데이터를 볼 때 가중치(weight) 값이 존재함
    # 이 부분은 가중치를 고려하여 경계선을 구분하기 위해 사용하는 부분임
    # 즉 0 혹은 1을 결정짓는 경계선을 만들기 위한 작업이라 정리할 수 있음
    # 예로 coef[0][0] 은 첫 번째 가중치(weight)
    # coef[0][1] 은 두 번째 가중치임
    # 그리고 intercept[0] 는 절편에 해당함
    # w1 * x1 + w2 * x2 + b = 0
    # w1x1 + w2x2 + b = 0
    # w2x2 = -w1x1 - b
    # x2 = -(w1x1 + b) / w2 <<<<

    # 0.5 = 1 / [1 + e^(w.x / b)]
    # ln -> w.x + b = 0
    # w1.x1 + w2.x2 + ... + b = 0
    y_values = -(coef[0][0] * x_values + intercept[0]) / coef[0][1]

    return JSONResponse(content={
        "accuracy": accuracy,
        "coefficients": coef.tolist(),
        "intercept": intercept.tolist(),
        "data_point": {
            "X": X.tolist(),
            "y": y.tolist()
        },
        "decision_boundary": {
            "x_values": x_values.tolist(),
            "y_values": y_values.tolist()
        }
    })
