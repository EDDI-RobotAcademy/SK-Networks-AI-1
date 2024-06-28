import os.path

import joblib
from fastapi import APIRouter, HTTPException, Query, Body
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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 훈련 모델 정의
    # Sequential() 을 통해 모델의 각 Layer를 순차적으로 구성함을 의미함
    # 즉 적혀있는 순서대로 다음 Layer를 타고 내려가게 됨
    # Dense() 의 경우 Fully Connected를 의미함
    # 첫 번째 Layer는 64개의 뉴런을 가지고 있고 입력 크기는 4개에 해당함
    # 여기서 입력 크기라는 것은 파라미터가 4개 존재한다는 것을 의미함
    # 활성 함수로 'relu'를 사용하는데 relu는 y = x와 같은 선형적인 특성을 가지고 있으면 사용하는 편
    # 그렇게 뉴런의 숫자를 줄여나가서 마지막에 활성 함수로 softmax를 사용함

    # Softmax의 정의는 아래와 같은데 사실 너무 장황하긴함
    # https://en.wikipedia.org/wiki/Softmax_function
    # Softmax를 사용하는 근본적인 이유는 입력 벡터를 확률 분포로 변환하기 위함임
    # 출력 베터의 각 요소는 자체적으로 구성한 분류에 속하는 확률 자체를 나타냄
    # 또한 각각의 확률들의 총합은 1이 됨
    # 수학적으로 확률 분포 함수를 전 구간에 걸쳐 적분하면 1이 되기 때문임 (100%)
    # 결국 Softmax를 사용하면 A일 확률 33%, B일 확률 33%, C일 확률 34% 형태로 값이 나온다는 소리
    # (물론 요따구로 나오면 사용할 수 없음)
    # A일 확률 98%, B일 확률 1%, C일 확률 1% 와 같은 형태라면 상당히 준수한 것
    # 하지만 지금 보면 여기서도 약점이 하나 있는데
    # 말도 안되는 없는 데이터를 넣는 경우에 대한 판정이 불가능함
    # 이것이 '세종 대왕님께서 훈민정음 창제하다 빡쳐서 맥북 던짐' 으로 연결됨
    
    # 부가적으로 우리가 사용하는 아래 형태가 결국 Nerual Network 라는 신경망에 해당함
    # Back Propagation(역전파)라는 것이 가능하려면 결국 함수 자체가 '미분 가능' 해야 하는데
    # exponential 함수 구성은 '미분 가능' 이므로 신경망에서 사용할 수 있음
    
    # 근데 생각보다 softmax 연산은 무거운편임
    # 시그마 + exponential 연산 때문
    # 일단 exponential은 오일러 공식을 생각해봐도 cos x + i sin x 형태를 띄기 때문에
    # 테일러 급수 전개를 해서 각각의 항들을 계산하고 팩토리얼 계산을 상수화하여 계산한다 하더라도
    # 최소 10차항까지는 계산을해줘야 근사치를 얻을 수 있기 때문에 연산 자체는 무거움
    # 이런 부분에서 GPU가 활약하면 성능을 상당히 많이 개선할 수 있음
    # 이 목적으로 논의되었던 것이 반도체 분야에선 NPU(Neural-network Processing Unit)
    # 혹은 DPU (Deep-learning Processing Unit) 라고 불러왔음
    # 현재 DPU / NPU 시장이 가장 큰 업체는 Apple에 해당함
    # 그리고 짐 켈러가 요즘 RISC V를 가지고 뭔가를 하려고해서 Nvidia 거품이 꺼질 전망임
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(4, activation='relu'),
        tf.keras.layers.Dense(3, activation='softmax')
    ])
    
    # 몇 가지 팁: 학습을 했을 때 데이터가 들쭉날쭉하는 경향을 보일 수 있음
    #            아무리 학습을 많이 해도 데이터 자체가 파동을 만든다는 뜻임 (수렴하지 않고)
    #            만약 이런 경우가 나타난다면 relu를 사용하지 말고 tanh 를 사용하는 것을 권장함
    #            기본적으로 하이퍼볼릭 탄젠트(tanh)의 경우 쌍곡선 함수로 cosh 와 sinh 로 구성됨
    #            그리고 하이퍼볼릭 함수들은 자체적으로 exponential을 가지고 있기 때문에
    #            위와 같은 곡선형 데이터, 파동형 데이터를 적합하는데 상당히 훌륭함
    #            단 위에서 거론했듯이 exponential이 많이 사용되면
    #            어쩔 수 없이 수치해석을 해야하기 때문에
    #            컴퓨터 내부적으로 테일러급수 전개가 강제되고 이로 인해 학습 시간은 길어짐
    #            단, 추론 성능은 상당히 좋아지게 됨
    #            어차피 우린 학습과 추론을 분리할 것이므로 필요하면 쓰는 것이 정답

    # 훈련 모델 컴파일
    # optimizer는 수동으로 커스텀하여 배치할 수도 있으나
    # 이러한 부분을 직접 조정하는 것을 하이퍼 파라미터 튜닝이라고 함
    # 우선은 기본적으로 쉽게 활용할 수 있는 모델로는 아래의 Adam 같은 것이 있음
    # 경사 하강법 기반을 사용하므로 학습 속도가 빠르고 보편적인 성능을 가짐
    # sparse_categorical_crossentropy의 경우 라벨이 정수로 인코딩 된 경우 다중 분류 문제에 적합함
    # 구성한 모델의 성능을 평가할 지표가 필요한데 해당 지표로 accuracy(정확도)를 사용
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    # 훈련 모델 학습
    # epochs는 몇 회 반복 학습을 시키느냐에 해당하는 수치입니다.
    # 500번 반복 학습을 시키니 iris 라는 꽃 분야에 상당한 대가로 거듭나게 훈련시키는 것
    model.fit(X_train, y_train, epochs=500, validation_data=(X_test, y_test))

    # 훈련된 모델 저장(학습 완료 상태)
    model.save(MODEL_PATH)

    # 모델 및 스케일러를 불러오기 위해 사용함 (joblib)
    joblib.dump(scaler, SCALER_PATH)
    joblib.dump(iris.target_names, CLASSIFICATION_PATH)
    
    return {"message": "Model / Scaler 훈련 완료"}

@tfIrisRouter.post('/tf-predict')
def predict(tfIrisRequestForm: TfIrisRequestForm):
    if (not os.path.exists(MODEL_PATH) or
            not os.path.exists(SCALER_PATH) or
            not os.path.exists(CLASSIFICATION_PATH)):
        raise HTTPException(status_code=400, detail="train부터 진행해주세요! 모델 및 스케일러 준비 안됨!")
    
    print("추론 진행")

    model = tf.keras.models.load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    classificationLabel = joblib.load(CLASSIFICATION_PATH)

    data = np.array([
        [
            tfIrisRequestForm.sepal_length,
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
