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

# response_model을 사용할 때
# return type이 등록한 type과 다르다면 에러 메시지가 출력됨
@trainTestEvaluationRouter.get("/train-test-evaluation", response_model=AnalysisResultResponseForm)
def train_test_evaluation():
    print("train_test_evaluation()")

    irisFlower = load_iris()
    X = irisFlower.data
    y = irisFlower.target

    print(f"X: {X}")
    print(f"y: {y}")

    # 내부 key값 확인
    print(f"irisFlower key: {irisFlower.keys()}")
    # feature 확인
    print(f"irisFlower feature: {irisFlower.feature_names}") # 특징값
    print(f"irisFlower feature: {irisFlower.target_names}") # 정답 (class)

    # 학습하기 (random_state : 재현률)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=42)
    # 정규화 (단위 벡터만드는 행위)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 로지스틱 회귀방식으로 훈련
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # 예측
    y_pred = model.predict(X_test)
    # 정확도 산출
    accuracy = accuracy_score(y_test, y_pred)
    # 혼동행렬로 표현
    confusionMatrix = confusion_matrix(y_test, y_pred).tolist()
    # 결과값 기록
    classReport = classification_report(y_test, y_pred, target_names=irisFlower.target_names,
                                         output_dict=True)
    print(f"accuracy: {accuracy}")
    print(f"confusionMatrix: {confusionMatrix}")
    print(f"classReport: {classReport}")

    selectedMetrics = [] # 몇번 case로 할것이냐?

    # 분류결과를 selectedMetrics에 저장
    for key in classReport.keys():
        if key in ['setosa', 'versicolor', 'virginica', 'macro avg','weighted avg']:
            selectedMetrics.append({
                "metric":key,
                "precision":classReport[key]['precision'],
                "recall": classReport[key]['recall'],
                "f1-score": classReport[key]['f1-score']
            })
    # Vue로 iris 분류 결과값 보내주기 (웹 상에서 주고받을 땐 무조건 JSON 변환한다 생각하기)
    return JSONResponse({
        "accuracy":accuracy,
        "confusion_matrix":confusionMatrix,
        "classification_report":selectedMetrics
    })