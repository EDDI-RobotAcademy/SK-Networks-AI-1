from gradient_descent.entity.linear_regression_model import LinearRegressionModel
from gradient_descent.repository.gradient_descent_repository import GradientDescentRepository

import tensorflow as tf
import numpy as np


class GradientDescentRepositoryImpl(GradientDescentRepository):
    RANGE_MAX = 100
    RANGE_MIN = 1
    RECALL = 42

    async def createTrainData(self):

        # 데이터를 생성할 때, np.random을 통해 임의의 노이즈 값을 만들어 준다.

        np.random.seed(self.RECALL)
        X = 2 * np.random.rand(self.RANGE_MAX, self.RANGE_MIN)
        y = 4 + 3 * X + np.random.rand(self.RANGE_MAX, self.RANGE_MIN)

        return X, y

    async def selectLinearRegressionModel(self):
        return LinearRegressionModel()

    async def calcMeanSquaredError(self, y_real, y_prediction):
        return tf.reduce_mean(tf.square(y_real - y_prediction))

    # Gradient Descent는 변화율이 최소가 되는 최적 경로를 찾기 위해 사용하는 편임
    # 그렇기 때문에 위와 같은 MSE(mean squared error) 계산이 진행됨
    # 좀 더 수식적으로 표현하면 origin - learningRate * ∇(origin_pred) 라고 볼 수 있음
    # ∇ 연산자의 경우 벡터의 도함수(벡터의 미분 연산자)로 단순히 d / dt 형태가 아님
    # 벡터이기 때문에 미분 연산자 자체가 Curl, Divergence, Gradient 3가지 형태로 나뉨
    # 그 중 Gradient가 2차원에서 다뤘던 기울기 d / dt 와 유사함
    # 고로 사실상 쉽게 생각하면 현재 (값 - 이전값 / 시간)
    # (이번값 - 이전값) / '뭔가 단위' 이런 느낌으로도 해석이 가능함
    # 결국 그 뭔지 모를 녀석의 기울기 값이라도 봐도 무방하겠음
    async def trainModel(self, selectedModel, X, y, learningRate=0.01, numEpoches=10000):
        X_tensor = tf.constant(X, dtype=tf.float32)
        y_tensor = tf.constant(y, dtype=tf.float32)

        print(f"selectedModel: {selectedModel}")

        for epoch in range(numEpoches):
            with tf.GradientTape() as tape:
                y_prediction = selectedModel(X_tensor)
                # 여기서 손실이 최소가 되는 것을 찾는 것임 (변화율 최소)
                loss = await self.calcMeanSquaredError(y_tensor, y_prediction)

            gradients = tape.gradient(loss, [selectedModel.weight, selectedModel.intercept])

            selectedModel.weight.assign_sub(gradients[0] * learningRate)
            selectedModel.intercept.assign_sub(gradients[1] * learningRate)

            if epoch % 100 == 0:
                print(f"Epoch: {epoch}, Loss: {loss.numpy()}")

        return selectedModel

    def loadModel(self, wantToBeLoadModel):
        print(f"repository -> loadModel()")
        model = LinearRegressionModel()

        data = np.load(wantToBeLoadModel)

        model.weight.assign(data['weight'])
        model.intercept.assign(data['intercept'])

        return model

    def predict(self, loadedModel, tensor):
        print(f"predict()")
        return loadedModel(tensor).numpy().tolist()
