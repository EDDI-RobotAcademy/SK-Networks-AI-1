from fastapi import APIRouter
from fastapi.responses import JSONResponse

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

logisticRegressionRouter = APIRouter()

@logisticRegressionRouter.get("/logistic-regression")
def logistic_regression_test():
    print("logistic_regression_test()")

    np.random.seed(0)
    X = np.random.randn(100, 2)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    # print('X:', X)
    # print('y:', y)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    coef = model.coef_
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