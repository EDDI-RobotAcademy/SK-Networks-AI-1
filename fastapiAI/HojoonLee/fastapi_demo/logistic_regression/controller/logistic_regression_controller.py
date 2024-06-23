# 현재 controller는 ddd 처럼 나누지 않고 단순 router 용도로만 사용할 것임
from fastapi import APIRouter
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from fastapi.responses import JSONResponse

# 아래와 같이 APIRouter를 가져오면
# 생성한 router 이름으로 get, post 등등의 router를 구성할 수 있음
# 얘는 곧 domain urls.py
logisticRegressionRouter = APIRouter()

@logisticRegressionRouter.get("/logistic-regression")
def logistic_regression_test():
    print("logistic_regression_test()")
    # 여기까지만으론 router 연결이 안 되므로 router include 작업을 해줘야 Vue랑 통신 가능

    np.random.seed(0)
    # 왜 x만 대문자? x는 단일 값이 아닌 여러 정보(열)를 담은 list() 라는 것을 상기해야함! X = [(1,2), (3,4) ... ]
    X = np.random.randn(100, 2) # 랜덤값으로 100행 2열의 데이터 생성 <=> (x,y) 2차원 벡터를 100개 생성
    y = (X[:,0] + X[:,1] > 0).astype(int) # x좌표와(0열) y좌표의(1열) 합이 0보다 크면 1 아니면 0
    print('X:', X)
    print('y:', y)

    # 데이터 분류하는 방법 (7 : 3비율로 train, test 나누겠다.)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    # 학습 모델로 Logisitc Regression을 선택, 모델은 sklearn에서 import 해야함
    model = LogisticRegression()
    # 테스트 외의 훈련 데이터를 가지고 실제 회귀 분석 진행
    model.fit(X_train, y_train)
    # 학습 시켰으니 test data로 예측하기
    y_pred = model.predict(X_test)
    # test data로 얼마나 맞았을까 ? => 예측과 정답 비교하기
    accuracy = accuracy_score(y_test, y_pred)
    coef = model.coef_ # coeeficient >> 계수 : Y = A*X + B 에서 A를 의미
    intercept = model.intercept_ # 절편 값 : B를 의미
    # 계수와 절편을 알기 때문에, x값만 주어지면 y를 알 수 있음

    # X(데이터)에 대한 기준을 설정! >> 과제와 엮으면 구매내역을 T/F 로 로지스틱회귀를 적용
    # X 값을 일정 범위로 설정
    # 100개의 X(x,y)의 x성분 중 최소값과 최대값을 뽑아서 일정 간격으로 분할 >> X[:,0](=x좌표)의 최소 최대만 활용함
    x_values = np.linspace(X[:,0].min(), X[:,0].max(), num=100) # x_values 는 이미 100개로 분할됨
    # 어떤 데이터를 볼 때 가중치(weight) 값이 존재함
    # 이 부분은 가중치를 고려하여 경계선을 구분하기 위해 사용하는 부분임
    # 즉, 0 혹은 1을 결정짓는 경계선을 만들기 위한 작업이라 정리할 수 있음
    # 예로 coef[0][0]은 첫 번째 가중치, coef[0][1]은 두 번째 가중치
    # y = A*X + b 이것도 사실 원본은 각 가중치가 적용된 w1*x + w2*y + b = 0 의 꼴임
    # w1*x + w2*y + b = 0  ==>  y = -(w1 * x1 + b)/ w2  를 표현하고 싶었던 것임
    # 하지만 여기선 X는 (x1, x2)라 (x,y)로 매핑된거고 나중엔 X는 (x1, x2 ..., xn)으로 되어 좀 다르게 생각해야할 듯?
    y_values = -(coef[0][0] * x_values + intercept[0]) / coef[0][1] # 왜 이런 식이 된걸까?

    # logistic_regression_test() 부분은 한번 정하면 바뀌지 않기 때문에 repository의 역할과 같다고 볼 수 있음
    return JSONResponse(content={
        "accuracy": accuracy,
        "coefficients": coef.tolist(),
        "intercept": intercept.tolist(),
        "data_point": {
            "X": X.tolist(),
            "y": y.tolist()
        },
        # decision boundary는 x_values, y_values를 의미
        "decision_boundary":{
            "x_values": x_values.tolist(),
            "y_values": y_values.tolist()
        }
    })