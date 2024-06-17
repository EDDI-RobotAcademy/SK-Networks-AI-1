from fastapi import APIRouter
from fastapi.responses import JSONResponse

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

#아래와 같이 APIRouter를 가져오면

logisticRegressionRouter = APIRouter()

@logisticRegressionRouter.get("/logistic-regression")
def logistic_regression_test():
    print("logistic_regression_test()")

    np.random.seed(0)
    # 임의의 (x,y) 2차원 벡터(좌표)를 100개 생성
    X = np.random.randn(100, 2)
    # x 좌표와 y좌표를 더해서 0크면 1, 아니면 0
    y = (X[:, 0] + X[:, 1] > 0).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    print('X:', X)
    print('y:', y)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # 테스트용 좌표를 가지고 결과값을 추론
    #  X = [(1,2),(3,4),(2,3),...]
    #  y = [ 1   ,  1  ,  1  , ...]
    y_pred = model.predict(X_test)

    # 예측치인 pred 값과 실제 테스트 셋인 test를
    # 비교하여 정확도가 어느정도인지 판별
    accuracy = accuracy_score(y_test, y_pred)
    coef = model.coef_
    intercept = model.intercept_

    x_values = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
    y_values = -(coef[0][0] * x_values + intercept[0] / coef[0][1])

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


