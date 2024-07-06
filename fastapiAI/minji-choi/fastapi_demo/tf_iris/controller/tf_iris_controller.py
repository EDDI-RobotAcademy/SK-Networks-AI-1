import os

import joblib
from fastapi import APIRouter, HTTPException, Body
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
from sklearn.datasets import load_iris

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from tf_iris.controller.request_form.tf_iris_request_form import TfIrisRequestForm

# from kmeans.controller.response_form.kmeans_cluster_response_form import KmeansClusterResponseForm

tfIrisRouter = APIRouter()
scaler = StandardScaler()
MODEL_PATH = 'tf_iris_model.h5'
SCALER_PATH = 'tf_iris_scaler.pkl'
CLASSIFICATION_NAME_PATH = 'tf_iris_classification_label.pkl'

@tfIrisRouter.get("/tf-train")

async def tfTrainModel():
    # 데이터 로드 (iris 데이터)
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 스케일러 적용
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 훈련 모델 정의
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(3, activation='softmax')
    ])

    # 훈련 모델 컴파일
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=100, validation_data=(X_test, y_test))

    # 훈련된 모델 저장(학습 완료 상태)
    model.save(MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    joblib.dump(iris.target_names, CLASSIFICATION_NAME_PATH)
    return {'message': "Model / Scaler 훈련 완료"}

@tfIrisRouter.post('/tf-predict')
def predict(tfIrisRequestForm: TfIrisRequestForm):
    # 학습된 모델 없으면 no
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH) or not os.path.exists(CLASSIFICATION_NAME_PATH):
        raise HTTPException(status_code=400, detail='모델 및 스케일러 준비 안됨')

    model = tf.keras.models.load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    classificationLabel = joblib.load(CLASSIFICATION_NAME_PATH)
    data = np.array([[
        tfIrisRequestForm.sepal_length,
        tfIrisRequestForm.sepal_width,
        tfIrisRequestForm.petal_length,
        tfIrisRequestForm.petal_width]])

    data = scaler.transform(data)
    prediction = model.predict(data)
    maxVal = np.argmax(prediction)
    predictedClass = classificationLabel[maxVal]
    print(f"prediction : {prediction}")
    print(f'해당 붓꽃은 : {predictedClass}')

    return {
        "prediction": prediction[0][maxVal].tolist(),
        'predicted_class': predictedClass
    }
