import joblib
from fastapi import APIRouter
from fastapi.responses import JSONResponse

import tensorflow as tf

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

tfIrisRouter = APIRouter()

MODEL_PATH = 'tf_iris_model.h5'
SCALER_PATH = 'tf_iris_scaler.pk1'

@tfIrisRouter.get("/tf-train")
async def tfTrainModel():
    # Iris 꽃 데이터 로드
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 훈련 모델 정의
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(4, activation='relu'),
        tf.keras.layers.Dense(3, activation='softmax')
    ])

    # 훈련 모델 컴파일
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    # 훈련 모델 학습
    model.fit(X_train, y_train, epochs=500, validation_data=(X_test, y_test))

    # 훈련된 모델 저장(학습 완료 상태)
    model.save(MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    
    return {"message": "Model / Scaler 훈련 완료"}
