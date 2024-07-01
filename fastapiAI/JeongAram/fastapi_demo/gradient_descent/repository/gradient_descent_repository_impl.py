from keras.src.models import model

from gradient_descent.entity.linear_regression_model import LinearRegressionModel
from gradient_descent.repository.gradient_descent_repository import GradientDescentRepository
import numpy as np
import tensorflow as tf


class GradientDescentRepositoryImpl(GradientDescentRepository):
    RANGE_MAX = 100
    RANGE_MIN = 1
    RECALL = 42

    async def createTrainData(self):
        np.random.seed(self.RECALL)
        # 가우시안 분포 1
        X = 2 * np.random.rand(self.RANGE_MAX, self.RANGE_MIN)
        # 가우시간 분포 2 -> 서로 종속관계
        y = 4 + 3 * X + np.random.rand(self.RANGE_MAX, self.RANGE_MIN)

        return X, y

    async def selectLinearRegressionModel(self):
        return LinearRegressionModel()

    async def calcMeanSquaredError(self, y_real, y_prediction):
        return tf.reduce_mean(tf.square(y_real - y_prediction))

    async def trainModel(self, selectedModel, X, y, learningRate=0.01, numEpochs=10000):
        X_tensor = tf.constant(X, dtype=tf.float32)
        y_tensor = tf.constant(y, dtype=tf.float32)

        # print(f"selectedModel: {selectedModel}")

        for epoch in range(numEpochs):
            with tf.GradientTape() as tape:
                y_prediction = selectedModel(X_tensor)
                # print(f"y_prediction: {y_prediction}")

                # 여기서 손실이 최소가 되는 것을 찾는 것임(변화율 최소)
                loss = await self.calcMeanSquaredError(y_tensor, y_prediction)

            gradients = tape.gradient(loss, [selectedModel.weight, selectedModel.intercept])
            print(f"gradients: {gradients}")

            selectedModel.weight.assign_sub(gradients[0] * learningRate)
            selectedModel.intercept.assign_sub(gradients[1] * learningRate)

            if epoch % 100 == 0:
                print(f"Epoch: {epoch}, Loss: {loss.numpy()}")

        return selectedModel

    def loadModel(self, wantToBeLoadModel):
        model = LinearRegressionModel()

        data = np.load(wantToBeLoadModel)

        model.weight.assign(data['weight'])
        model.intercept.assign(data['intercept'])

        return model

    def predict(self, loadedModel, tensor):
        return loadedModel(tensor).numpy().tolist()


