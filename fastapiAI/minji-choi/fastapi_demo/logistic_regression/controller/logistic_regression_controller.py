from fastapi import APIRouter
from fastapi.responses import JSONResponse

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # random_state가 0이면 재현율이 100이 됨

    print('X:', X)
    print('y:', y)

    # 학습 모델로 Logistic Regression을 선택
    model = LogisticRegression()
    # 테스트 외의 훈련 데이터를 가지고 실제 회귀 분석 진행
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    coef = model.coef_
    # y = ax + b에서 intercept_ 는 b를 의미함
    intercept = model.intercept_

    x_values = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
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