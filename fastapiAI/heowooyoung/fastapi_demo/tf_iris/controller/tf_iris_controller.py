import os.path

import joblib
from fastapi import APIRouter, HTTPException, Query, Body
from fastapi.responses import JSONResponse

import tensorflow as tf
import numpy as np

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import  accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from tf_iris.controller.request_form.tf_iris_request_form import TfIrisRequestForm

tfIrisRouter = APIRouter()

MODEL_PATH = 'tf_iris_model.h5'
SCALER_PATH = 'tf_iris_scaler.pk1'
CLASSIFICATION_PATH = 'tf_iris_classification_label.pk1'
# CLASSIFICATION_NAME = None

@tfIrisRouter.get("/tf-train")
async def tfTrainModel():

    # Iris 꽃 데이터 로드
    iris = load_iris()

    # global CLASSIFICATION_NAME
    # CLASSIFICATION_NAME = iris.target_names

    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    # 훈련 모델 정의
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(4, activation='relu'),
        tf.keras.layers.Dense(3, activation='softmax'),
    ])

    # 훈련 모델 컴파일
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    # 훈련 모델 학습
    model.fit(X_train, y_train, epochs=500, validation_data=(X_test, y_test))

    # 훈련된 모델 저장(학습 완료 상태)
    model.save(MODEL_PATH)

    # 모델 및 스케일러를 불러오기 위해 사용함 (joblib)
    joblib.dump(scaler, SCALER_PATH)
    joblib.dump(iris.target_names, CLASSIFICATION_PATH)

    return { "message": "Model / Scaler 훈련 완료"}

@tfIrisRouter.post('/tf-predict')
def predict(tfIrisRequestForm: TfIrisRequestForm):
    if (not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH) or not os.path.exists(CLASSIFICATION_PATH)):
        raise HTTPException(status_code=400, detail="train부터 진행해주세요! 모델 및 스케일러 준비 안됨!")

    print("추론 진행")

    model = tf.keras.models.load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    classificationLabel = joblib.load(CLASSIFICATION_PATH)

    data = np.array([
        [    tfIrisRequestForm.sepal_length,
             tfIrisRequestForm.sepal_width,
             tfIrisRequestForm.petal_length,
             tfIrisRequestForm.petal_width,
        ]
    ])

    data = scaler.transform(data)
    prediction = model.predict(data)
    print(f"prediction: {prediction}")
    whichOneIsMax = np.argmax(prediction)
    print(f"which one is max ? whichOneIsMax")

    predictedClass = classificationLabel[np.argmax(prediction)]
    print(f"predictedClass: {predictedClass}")

    return {
        "prediction": prediction[0][whichOneIsMax].tolist(),
        "predicted_class": predictedClass
    }