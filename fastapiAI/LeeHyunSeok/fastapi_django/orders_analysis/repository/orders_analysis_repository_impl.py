from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from orders_analysis.repository.orders_analysis_repository import OrdersAnalysisRepository

import tensorflow as tf

class OrdersAnalysisRepositoryImpl(OrdersAnalysisRepository):

    # viewCount와 quantity 열을 추출하여 독립변수 x와 종속 변수 y로 사용
    # StandardScaler()를 통해 표준화(Normalization)
    async def prepareViewCountVsQuantity(self, dataFrame):
        X = dataFrame['viewCount'].values.reshape(-1, 1)   #dataFrame[''] 안에 칼럼을 넣으면 그 칼럼의 값들을 다 가져온다. / reshape는 칼럼은 세로(열)이니 가로(행)으로 바꿔주는 함수
        y = dataFrame['quantity'].values

        scaler = StandardScaler()   # 스탠다드스케일러는 정규분포
        X_scaled = scaler.fit_transform(X)

        return X_scaled, y, scaler


    # 데이터 전체 중 훈련 집합으로 80%, 테스트 목적으로 20%를 구성함
    # test_size는 테스트를 위한 데이터의 비율
    # X_train, X_test, y_train, y_test <- 이 순서대로 써주는거 중요함
    async def splitTrainTestData(self, X_scaled, y):
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )

        return X_train, X_test, y_train, y_test


    # Keras Sequential 모델 생성
    # 입력 크기가 1인 입력층을 구성하고 Dropout을 사용하여 일정 데이터를 버렸음
    # 현재 상황이 데이터 특정이 안되기 때문에 Dropout울 버리는 것은 사실 다소 위험할 수 있음
    # keras는 텐서플로 안에 있는 인공신경망을 쌓는 모듈임. 무조건 텐서플로우랑 세트로 쓰인다.
    # Sequential 인공신경망의 포장지 같은 것.
    # Dense는 히든레이어의 갯수이다.
    # activation는 활성함수이다. 활성함수는 비선형성을 준다. / relu의 장점: 연산이 빠르다.
    # relu와 tanh를 함께 쓴 이유는 relu는 0보다 작으면 다 밀어버리기 때문에 만약 0보다 작은 수가 있으면 없어지니 tanh를 섞어서 0보다 작은 수가 조금이라도 살아남게 만든 것임.
    async def createModel(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(128, activation='relu', input_shape=(1,)),
            tf.keras.layers.Dropout(0.3),  # Dropout은 내가 가지고 있는 데이터를 버리는 것임. 왜? 과적합을 방지하기 위헤.
            tf.keras.layers.Dense(64, activation='relu'), tf.keras.layers.Dropout(0.2), # 과적합 방지를 위해 20%는 버리도록 설정
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


        # 다음 fit할때 optimizer는 뭘로 할지, loss는 뭘로 계산할지, metrics는 뭘로할지 미리 설정해두는 코드
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), # learning_rate는 어떠한 수로 수렴하는 속도임. 너무 크면 목표점을 넘어갈수 있을 수 있고, 반대로 낮게 하면 목표점에 도달은 하지만 속도가 느림
            loss='mean_squared_error',
            # metrics은 측정 기준임
            metrics=['mae']
        )

        return model


    # 실제 모델에 대한 fit을 할때 학습하는 과정 자체
    # 이 과정 자체를 보여주고자 한다면 verbose를 1로 설정하면 됨
    async def fitModel(self, model, X_train, y_train):  # 만든 모델을 진짜 학습시키는 부분(model.fit을 해야 학습을 하는 것임.)
        model.fit(X_train,
                  y_train,
                  epochs=100,       #epochs는 몇 번 반복할 것이냐임
                  validation_split=0.2,     # validation_split=0.2는 80%의 훈련 데이터 중 다시 20%를 따로 빼서 훈련이 끝난 후 세미 수능을 보는 느낌으로 테스트를 한 번 하는 거임/ validation_split이 없어도 돌아가지만 있어야 optimizer가 더 옳바른 학습법을 찾기 수월함
                  batch_size=32,        # batch_size=32는 한 번의 epochs당 할 학습량 즉, 저건 한 번의 epochs당 32개의 데이터를 학습 하겠다는 뜻.
                  verbose=0)        # verbose=0이면 중간과정이 생략된다. / 중간과정이란? epochs안에서 일어나는 일 / verbose=1로 하면 loss값이나 그런 것이들 매 epochs마다 어떻게 변화하는지 나옴



    # 입력 데이터를 스케일링함
    # StandardScaler로 만들어진 것을 joblib을 이용해서 저장했었음
    # 이를 사용하여 0~1 사이의 정규 분포 구성으로 설정함
    # 즉, 반환값은 x_pred라는 녀석을 0~1 사이로 정규화한 데이터 리스트
    async def transformFromScaler(self, scaler, X_pred):
        return scaler.transform(X_pred)


    # 훈련된 keras Model을 사용하여 실질적인 예측을 진행함
    # 실제로 predict()는 2D배열을 반환하는데
    # flatten()을 사용하여 1D배열로 변경하여 첫 번째 요소를 반환   <-중요 다시 공부헤보기
    async def predictFromModel(self, ordersModel, X_pred_scaled):
        return ordersModel.predict(X_pred_scaled).flatten()[0]