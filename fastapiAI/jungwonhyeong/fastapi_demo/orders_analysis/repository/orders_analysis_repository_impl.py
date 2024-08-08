from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from orders_analysis.repository.orders_analysis_repository import OrdersAnalysisRepository

import tensorflow as tf


class OrdersAnalysisRepositoryImpl(OrdersAnalysisRepository):

    async def prepareViewCountVsQuantity(self, dataFrame):
        X = dataFrame['viewCount'].values.reshape(-1, 1)
        y = dataFrame['quantity'].values

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        return X_scaled, y, scaler

    async def splitTrainTestData(self, X_scaled, y):
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )

        return X_train, X_test, y_train, y_test

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

    async def fitModel(self, model, X_train, y_train):
        model.fit(X_train,
                  y_train,
                  epochs=500,
                  validation_split=0.2,
                  batch_size=32,
                  verbose=1)

    async def transformFromScaler(self, scaler, X_pred):
        return scaler.transform(X_pred)

    async def predictFromModel(self, ordersModel, X_pred_scaled):
        return ordersModel.predict(X_pred_scaled).flatten()[0]