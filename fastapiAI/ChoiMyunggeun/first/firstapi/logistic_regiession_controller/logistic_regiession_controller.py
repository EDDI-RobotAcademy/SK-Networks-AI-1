from fastapi import APIRouter
from fastapi.responses import JSONResponse

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

# 에이피아이라우터 는 겟 포스트 등의 라우터를구성할수있댐
logisticRegiessionRouter = APIRouter()

@logisticRegiessionRouter.get("/logistic-regression")
def logistic_regression_test():
    print("logistic_regression_test()")

    np.random.seed(42)
    # 임의의 2차원 벡터를 100개를 생성
    # 아마 가상데이터로 학습시키려는듯
    X = np.random.randn(100,2)
    # X 좌표와 y 좌표를 더해서 양수는1 음수는0 이런식으로
    # 근데 이럴거면 룰베이스가 낫지않나.. 오차나 노이즈 껴줘야지
    y = (X[:, 0] + X[:, 1] > 0).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    print('X:',X)
    print('y:', y)
    # 리그레션은 오차를 판별하기 위해 특정방향 도함수를 이용함
    # 정규분포는 e^(-x^2)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    coef = model.coef_
    intercept = model.intercept_

    x_values = np.linspace(X[:, 0].min(), X[:, 0].max(), num=100)
    # coef 는 여러 가중치집합, intercept 는 절편
    #
    y_values = -(coef[0][0] * x_values + intercept[0]) / coef[0][1]

    return JSONResponse(content={
        "acc": accuracy,
        "coefficients": coef.tolist(),
        'intercept': intercept.tolist(),
        'data_point': {
            'X': X.tolist(),
            'y': y.tolist(),
        },
        'decision_boundary': {
            'x_values': x_values.tolist(),
            'y_values': y_values.tolist(),
        }
    })
