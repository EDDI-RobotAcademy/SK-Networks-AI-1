from fastapi import APIRouter
from fastapi.responses import JSONResponse
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# 아래와 같이 APIRouter를 가져오면
# 생성한 router 이름으로 get, post 등등의 router를 구성할 수 있음
# 이는 곧 domian urls.py
logisticRegressionRouter = APIRouter()

@logisticRegressionRouter.get("/logistic-regression")
def logistic_regression_test():
    print("logistic_regression_test()")
    # router include하는 작업이 필요하다. 위의 코드만으로는 안됨.


    np.random.seed(0)
    # 임의의 (x, y) 2차원 벡터(좌표)를 100개 생성
    X = np.random.randn(100,2)
    y = (X[:, 0] + X[:, 1] > 0).astype(int) # x와 y좌표를 더한 것이 0보다 크면 1, 아니면 0
    # 자동으로 100개 중 30%를 테스트셋으로 지정함
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    print('X: ', X)
    print('y: ', y)

    # 학습모델로 Logistic Regression을 선택
    model = LogisticRegression()
    # 테스트 외의 훈련 데이터를 가지고 실제 회귀 분석 진행
    model.fit(X_train, y_train)
    # 회귀 분석이란?
    # 결론적으로 Y = A.X + B 를 찾는 수학적인 기법이라 볼 수 있음
    # 기본적으로 증명을 위해서 편미분을 사용해야 하나 여기는 수학 학원이 아니니 배제
    # 기본적인 접근은 x 값에 대해 최소 오차가 얼마인지, y 값에 대한 최소 오차가 얼마인지를 판별하기 위해
    # 특정 방향 도함구(편미분)을 사용해야 하는 것임
    # 미분=변화율
    # 변화가 얼마나 작게 일어나는가를 기준으로 함수를 어떻게 만들 것인가 추적하는 기법

    # 테스트용 좌표를 가지고 결과값을 추론
    # X가 벡터 리스트(좌표) 실제로 X가 행렬표현
    # X = [(1,2),(3,4),...]
    # y = [  1,    1,  ...]
    # y는 열벡터
    y_pred = model.predict(X_test) # X안에 있는 것중 30%를 테스트
    # 예측치인 pred 값과 실제 테스트 셋인 test를 비교하여 정확도가 어느정도인지 판별
    accuracy = accuracy_score(y_test, y_pred) # y_pred(실제값)가 y의 30%와 얼만큼 일치하는지
    # y = ax + b라 가정 했을 때 coef_는 a를 의미함 intercept_는 b를 의미함
    # 계수값과 절편값을 알고 있으니까 x값을 넣으면 y값이 나옴
    # logistic 회귀분석이기 때문에 y는 0이나 1이 나옴
    coef = model.coef_ # 계수값
    intercept = model.intercept_ # 절편값

    # x 값을 일정 범위로 설정
    # linspace - 100개의 x 성분 중 최소값과 최대값을 뽑아서 일정 간격으로 분할
    # 최소와 최대가 있으니까 100등분 가능
    x_values = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
    # 어떤 데이터를 볼 때 가중치(weight) 값이 존재함
    # 이 부분은 가중치를 고려하여 경계선을 구분하기 위해 사용하는 부분임
    # 즉 0 혹은 1을 결정짓는 경계선을 만들기 위한 작업이라 정리할 수 있음
    # 예로 coef[0][0]은 첫번째 가중치(weight)
    # coef[0][1]은 두번째 가중치
    # intercept[0]는 절편
    # w1 * x1 + w2 * x2 + b = 0
    # w1x1 + w2x2 + b = 0
    # w2x2= -w1x1 - b =0
    # x2 = -(w1x1 + b) / w2
    # 0.5 = 1 / [1 + e^(w.x / b)]
    # ln -> w.x + b = 0
    # w1.x1 + w2.x2 + ... + b = 0
    y_values = -(coef[0][0] * x_values + intercept[0]) / coef[0][1] # x_values는 이미 100개로 분할되어 있음
    # 이 계산식은 역할로 치면 repository 역할
    # 따라서 만들어놓고 바꿀 일이 없기 때문에 갖다 쓰면 된다.
    # repository는 세부사항이기 때문에 자세히 알 필요가 없다.
    # 비즈니스 아젠다에서 '뭘 써서 뭘 할꺼야' 중 '뭘 할꺼야'가 중요하기 때문

    # 그래프 그릴때 정확도, 계수값, 절편, 어떤 데이터들에 대한 그래프인지 판정, x_values y_values 어디 경계를 기준으로 나뉘나
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
    #이 정보들로 vue에서 표현한다.
