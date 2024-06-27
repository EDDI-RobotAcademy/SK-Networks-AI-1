import os.path

import joblib
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

import tensorflow as tf

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from tf_iris.controller.request_form.tf_iris_request_form import TfIrisRequestForm

tfIrisRouter = APIRouter()

MODEL_PATH = 'th_iris_model.h5'
SCALER_PATH = 'th_iris_scaler.pk1'
# CLASSIFICATION_NAME = None
CLASSIFICATION_PATH = 'tf_iris_classification_label.pkl'

@tfIrisRouter.get("/tf-train")
async def tfTraionModel():
    iris = load_iris()
    global CLASSIFICATION_NAME
    CLASSIFICATION_NAME = iris.target_names
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=100, validation_data=(X_test, y_test))

    model.save(MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    joblib.dump(iris.target_names, CLASSIFICATION_PATH)

    return {'message':'Model/ Scaler 훈련 완료'}

@tfIrisRouter.post('/tf-predict')
def predict(tfIrisRequestForm: TfIrisRequestForm):
    if (not os.path.exists(MODEL_PATH) or
            not os.path.exists(SCALER_PATH) or
            not os.path.exists(CLASSIFICATION_PATH)):
        raise HTTPException(status_code=400, detail='학습부터 진행해 주세요 모델 및 스케일러 준비 안됨')
    print('추론 진행')

    model = tf.keras.models.load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    classificationLabel = joblib.load(CLASSIFICATION_PATH)

    data = np.array(([
        [
            tfIrisRequestForm.sepal_length,
            tfIrisRequestForm.sepal_width,
            tfIrisRequestForm.petal_width,
            tfIrisRequestForm.petal_length,
        ]
    ]))

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