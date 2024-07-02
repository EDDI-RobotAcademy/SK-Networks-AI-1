from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf


from orders_analysis.repository.orders_analysis_repository import OrdersAnalysisRepository


class OrdersAnalysisRepositoryImpl(OrdersAnalysisRepository):
    async def prepareViewCountVsQuantity(self, dataFrame):
        X = dataFrame['viewCount'].values.reshape(-1, 1)
        y = dataFrame['quantity'].values

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        return X_scaled, y, scaler

    async def splitTrainTestData(self, X_scaled, y):
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size = 0.2, random_state = 42
        )

        return X_train, X_test, y_train, y_test


    async def createModel(self):
        model = tf.keras.models.Seauential([
            tf.keras.layers.Dense(128, activation='relu', input_shape=(1,)),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(64, activation='relu'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(64, activation='tanh'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32, activation='relu'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32, activation='tanh'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(16, activation='relu'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(16, activation='tahn'), tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(8, activation='relu'),
            tf.keras.layers.Dense(8, activation='tanh'),
            tf.keras.layers.Dense(4, activation='relu'),
            tf.keras.layers.Dense(4, activation='tanh'),
            tf.keras.layers.Dense(2, activation='relu'),
            tf.keras.layers.Dense(2, activation='tanh'),
            tf.keras.layers.Dense(1)
        ])

        model.compile(
            optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001),
            loss = 'mean_squared_error',
            metrics = ['mae']
        )

        return model

    async def fitModel(self, model, X_train, y_train):
        model.fit(X_train,
                  y_train,
                  epochs=2000,
                  validation_split=0.2,
                  batch_size=32,
                  verbose=1)

    # 입력 데이터를 스케일링함
    # StandardScaler로 만들어진 것을 joblib을 이용해서 저장했었음
    # 이를 사용하여 0 ~ 1 사이의 정규 분포 구성으로 설정함
    # 즉 반환 값은 x_pred라는 녀석을 0 ~ 1 사이로 정규화한 데이터 리스트
    async def transformFromScaler(self, scaler, X_pred):
        return scaler.transform(X_pred)

    # 훈련된 Keras Model을 사용하여 실질적인 예측을 진행함
    # 실제로 predict()는 2D 배열을 반환하는데
    # flatten()을 사용하여 1D 배열로 변경하여 첫 번째 요소를 반환
    async def predictFromModel(self, ordersModel, X_pred_scaled):
        return ordersModel.predict(X_pred_scaled).flatten()[0]