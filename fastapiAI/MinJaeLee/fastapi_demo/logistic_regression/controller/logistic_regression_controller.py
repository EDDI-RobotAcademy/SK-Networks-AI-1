from fastapi import APIRouter
from fastapi.responses import JSONResponse
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

logisticRegressionRouter = APIRouter()

@logisticRegressionRouter.get("/logistic regression")
def logistic_regression_test():
    print("logistic_regression_test()")

    np.random.seed(0)
    # 임의의 x, y 2차원 벡터를 100개 생성
    X = np.random.randn(100, 2)
    # x 좌표와 y좌표를 더해서 0보다 크면 1, 아니면 0
    y = (X[:,0] + X[:, 1] > 0).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
    print('X' , X)
    print('y' , y)

    model = LogisticRegression()

    model.fit(X_train, y_train)

    # 회귀 분석이란?
    # 결론적으로 Y = A.X+B를 찾는 수학적인 기법이라 볼 수 있음
    # 기본적으로 증명을 위해선 편미분을 사용해야 하나... 여기는 수학 학원이 아니니 배제
    # 기본적인 접근은 x 값에 대해 최소 오차가 얼마인지, y 값에 대한 최소 오차가 얼마인지를 판별하기 위해
    # 특정 방향 도함수(편미분)을 사용해야 하는 것임
    # 미분하니 사실 좀 어질어질 할 수 있는데 복잡하게 생각할 필요 없이 미분은 변화율이라 생각하면 됨
    # 그러니 변화가 얼마나 적게 일어나는가를 기준으로
    # 함수를 어떻게 만들 것인가 추적하는 기법으로 정리할 수 있음

    # 그래프 추이를 보고 싶다면 https://www.wolframalpha.com/
    # 여기서 그냥 함수 형태를 입력하면 알아서 그려줌

    # 결론적으로 회귀 분석에 여러 종류가 있는 이유는 여러 다양한 형태의 그래프를 표현하기 위해서임
    # 그리고 그 판단은 어쩔 수 없이 사람이 결정해줘야함
    # 무엇이 이 데이터에 더 적합한지
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    # y = ax + b 일때 a를 의미
    coef = model.coef_
    # y = ax + b 일때 b를 의미
    intercept = model.intercept_

    # x 값을 일정 범위로 설정
    # 100개의 x 성분 중 최소값과 최대값을 뽑아서 일정 간격으로 분할
    x_values = np.linspace(X[:,0].min(), X[:,0].max(), 100)
    # 어떤 데이터를 볼 때 가중치(weight)값이 존재함
    # 이 부분은 가중치를 고려하여 경계선을 구분하기 위해 사용하는 부분임
    # 즉 0 혹은 1을 결정짓는 경계선을 만들기 위한 작업이라 정리할 수 있음
    # 예로 coef[0][0] 은 첫 번째 가중치(weight)
    # coef[0][1]은 두 번째 가중치임
    # 그리고 inetercept[0]는 절편에 해당함
    # w1 * x1 + w2 * x2 + b = 0
    # x2 = -(w1 * x1 + b)/ w2
    y_values = -(coef[0][0] * x_values + intercept[0] / coef[0][1])

    return JSONResponse(content={
        "accuracy": accuracy,
        "coefficients":coef.tolist(),
        "intercept":intercept.tolist(),
        "data_point":{
            "x":X.tolist(),
            "y":y.tolist()
        },
        "decision_boundary":{
            "x_values":x_values.tolist(),
            "y_values":y_values.tolist()
        }
    })