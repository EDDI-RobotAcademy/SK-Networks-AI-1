from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from orders_analysis.repository.orders_analysis_repository import OrdersAnalysisRepository

import tensorflow as tf

# 인공신경망(Artificial Nerual Network)는 사람의 뇌 신경망을 모방하여 만들어진 시스템입니다.
# 패턴 인식 및 데이터 분류와 같은 작업에서 사용되며 기계 학습과 딥러닝에 있어 중요합니다.

# 뉴런 <- 여러 신호를 입력 받음
# 우리가 작성한 코드에선 input_shape에 해당함
# 가중치 <- 각 입력에 가중치가 존재하여 학습하면서 이 값이 조정됨
# 활성함수 <- 입력의 총합을 처리하여 최종 결과를 얻는데 사용함
#            대표적인 녀석으로 sigmoid, ReLU, tanh, softmax 같은 것들이 있음

# Layer는 Input Layer, Hidden Layer, Output Layer로 구성됩니다.
# 입출력은 유일하지만 Hidden Layer는 더 다양하게 많이 구성 될 수 있습니다.
# 위의 input_shape이 Input Layer에서 지정되어야 합니다.

# 시그모이드는 출력을 0 ~ 1 사이로 압축합니다.
# 즉 확률을 계산하기 위한 목적으로 사용합니다.
# ReLU는 입력 값이 0 보다 작으면 0 크면 값을 그대로 유지합니다.
# tanh의 경우 값을 -1 ~ 1 사이로 압축합니다.
# 이와 같은 특성 때문에 데이터가 요동치는 경우에 적합합니다.

# 보편적으로 ANN을 구성하는 방법은 아래와 같습니다.
#
# 1. 먼저 학습할 데이터를 확보합니다.
# 2. 전처리를 진행합니다(쓸대없는 데이터, 이상치들 제거)
# 3. 요상한 데이터가 없다면 신경망을 구성합니다.
# 4. 구성한 신경망으로 학습을 진행합니다.
# 5. 추론 시 빠르게 활용할 수 있도록 학습 정보를 저장합니다 (*.h5, *.keras)
# 6. 추론을 요청하면 앞서 저장한 *.h5 및 *.keras 에서 정보를 읽어서 빠르게 응답합니다.

# CNN: 컨볼루션 기반 신경망 -> 이미지 처리에 적합함
# RNN: 피드백이 포함된 구조로 시간 순서가 있는 경우에 적합함
class OrdersAnalysisRepositoryImpl(OrdersAnalysisRepository):

    # viewCount와 quantity 열을 추출하여 독립 변수 X와 종속 변수 y로 사용
    # StandardScaler()를 통해 표준화(Normalization)
    async def prepareViewCountVsQuantity(self, dataFrame):
        X = dataFrame['viewCount'].values.reshape(-1, 1)
        y = dataFrame['quantity'].values

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        return X_scaled, y, scaler

    # 데이터 전체 중 훈련 집합으로 80%, 테스트 목적으로 20%를 구성함
    async def splitTrainTestData(self, X_scaled, y):
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )

        return X_train, X_test, y_train, y_test

    # Keras Sequential 모델 생성
    # 입력 크기가 1인 입력층을 구성하고 Dropout을 사용하여 일정 데이터를 버렸음
    # 현재 상황이 데이터 특정이 안되기 때문에 Dropout을 버리는 것은 사실 다소 위험 할 수 있음
    async def createModel(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(128, activation='relu', input_shape=(1,)),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(64, activation='relu'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(64, activation='tanh'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32, activation='relu'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32, activation='tanh'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(16, activation='relu'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(16, activation='tanh'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(8, activation='relu'),
            tf.keras.layers.Dense(8, activation='tanh'),
            tf.keras.layers.Dense(4, activation='relu'),
            tf.keras.layers.Dense(4, activation='tanh'),
            tf.keras.layers.Dense(2, activation='relu'),
            tf.keras.layers.Dense(2, activation='tanh'),
            tf.keras.layers.Dense(1)
        ])

        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            loss='mean_squared_error',
            metrics=['mae']
        )

        return model

    # 실제 모델에 대한 fit을 할 때 학습하는 과정 자체
    # 이 과정 자체를 보여주고자 한다면 verbose를 1로 설정하면 됨
    async def fitModel(self, model, X_train, y_train):
        model.fit(X_train,
                  y_train,
                  epochs=500,
                  validation_split=0.2,
                  batch_size=32,
                  verbose=1)

    # 입력 데이터를 스케일링함
    # StandardScaler로 만들어진 것을 joblib을 이용해서 저장했었음
    # 이를 사용하여 0 ~ 1 사이의 정규 분포 구성으로 설정함
    # 즉 반환 값은 x_pred 라는 녀석을 0 ~ 1 사이로 정규화한 데이터 리스트
    async def transformFromScaler(self, scaler, X_pred):
        return scaler.transform(X_pred)

    # 훈련된 Keras Model을 사용하여 실질적인 예츠을 진행함
    # 실제로 predict()는 2D 배열을 반환하는데
    # flatten()을 사용하여 1D 배열로 변경하여 첫 번째 요소를 반환
    async def predictFromModel(self, ordersModel, X_pred_scaled):
        return ordersModel.predict(X_pred_scaled).flatten()[0]
