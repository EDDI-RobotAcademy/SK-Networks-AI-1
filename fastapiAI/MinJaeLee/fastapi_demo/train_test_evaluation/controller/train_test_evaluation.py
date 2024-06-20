from fastapi import APIRouter
from fastapi.responses import JSONResponse

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from train_test_evaluation.controller.response_form.analysis_result_response_form import AnalysisResultResponseForm

trainTestEvaluationRouter = APIRouter()

# Response, ResponseForm, Request, RequestForm
# response model을 사용할 때
# 리턴 타입이 등록한 타입과 다르면 에러 메시지가 출력됨
@trainTestEvaluationRouter.get("/train-test-evaluation", response_model=AnalysisResultResponseForm)
def train_test_evaluation():
    print("train_test_evaluation()")
    irisFlower = load_iris()
    X = irisFlower.data
    y = irisFlower.target

    print(f"X:{X}")
    print(f"y:{y}")

    print(f"irisFlower key: {irisFlower.keys()}")
    print(f"irisFlower feature: {irisFlower.feature_names}")
    print(f"irisFlower target: {irisFlower.target_names}")

    X_train, X_test, y_train, y_test = (train_test_split(X, y, test_size=0.1, random_state=42))

    # normalization
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # logistic regression training
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # prediction
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    confusionMatrix = confusion_matrix(y_test, y_pred).tolist()
    class_report = classification_report(y_test, y_pred, target_names = irisFlower.target_names, output_dict = True)

    print(f"accuracy: {accuracy}")
    print(f"confusionMatrix: {confusionMatrix}")
    print(f"class_report: {class_report}")

    selected_metrics = []

    for key in class_report.keys():
        if key in ['setosa', 'versicolor', 'virginica', 'macro avg', 'weighted avg']:
            selected_metrics.append({
                "metric":key,
                "precision":class_report[key]['precision'],
                "recall":class_report[key]['recall'],
                "f1-score":class_report[key]['f1-score'],
            })

    # 웹 페이지 상에서 정보를 주고 받을땐 그냥 무조건 JSON 변환이다 생각하면 됨.
    return JSONResponse({
        "accuracy":accuracy,
        "confusion_matrix":confusionMatrix,
        "classification_report":selected_metrics
    })