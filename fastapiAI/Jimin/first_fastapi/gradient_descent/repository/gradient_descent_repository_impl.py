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
        # np.random.rand(self.RANGE_MAX, self.RANGE_MIN): 가우시안 분포
        X = 2 * np.random.rand(self.RANGE_MAX, self.RANGE_MIN)
        # 마지막에 더해준 랜덤값이 노이즈 값이다. np.random.rand(self.RANGE_MAX, self.RANGE_MIN) 이것도 가우시안 분포
        # 노이즈가 없으면 처음부터fit하기 때문에 학습하는 의미가 없다.
        # 그래서 노이즈를 넣어줬다.
        y = 4 + 3 * X + np.random.rand(self.RANGE_MAX, self.RANGE_MIN)

        return X, y

    async def selectLinearRegressionModel(self):
        return LinearRegressionModel()
    # 우리가 만들어준 수식이 선형이라 회귀할때 linear 방식으로 예측하겠다.
    # y = 3X + 4, >>> w=3, b=4

    async def calcMeanSquaredError(self, y_real, y_prediction):
        return tf.reduce_mean(tf.square(y_real - y_prediction))

    # Gradient Descent는 변화율이 최소가 되는 최적 경로를 찾기 위해 사용하는 편임
    # 그렇기 때문에 위와 같은 MSE(mean squared error) 계산이 진행됨
    # 좀 더 수식적으로 표현하자면 origin - learningRate * ▽(origin_pred) 라고 볼 수 있음
    # ▽ 연산자의 경우 벡터의 도함수(벡터의 미분 연산자)로 단순히 d/dt 형태가 아님
    # 벡터이기 때문에 미분 연산자 자체가 Curl, Divergence, Gradient 3가지 형태로 나뉨
    # 그 중 Gradient가 2차원에서 다뤘던 기울기 d/dt와 유사함
    # 고로 사실상 쉽게 생각하면 현재 (값 - 이전값 / 시간)
    # (이번값 - 이전값) / '뭔가 단위' 이런 느낌으로도 해석이 가능함
    # 결국 그 뭔지 모를 녀석의 기울기 값이라고 봐도 무방함
    async def trainModel(self, selectedModel, X, y, learningRate=0.01, numEpoches=10000): # 값을 지정해줬기 때문에 인자를 더 선언 할 수 있다.
        # list를 numpy화하고 (numpy화해야 tensor로 바꿀 수 있다.) 그걸 tensor로 만들 수 있다.
        # tf.constant가 np.array를 tf.Tensor로 바꿔주는 기능
        # np도 행렬 tf도 행렬인데 하나의 자료형(Type)들이다.
        # list는 처리 속도가 느리기 때문에 안쓴다.
        # type 마다 할 수 있는 일들이 다르기 때문에 분류해서 쓴다.
        X_tensor = tf.constant(X, dtype=tf.float32)
        y_tensor = tf.constant(y, dtype=tf.float32)

        for epoch in range(numEpoches):
            with tf.GradientTape() as tape:
                y_prediction = selectedModel(X_tensor) # train data X를 y_pred에 넣은것
                # step1. 매 epoch마다 loss 구하기
                # 여기서 손실이 최소가 되는 것을 찾음 (변화율 최소)
                # loss 표현에도 여러개가 있는데, crossEntropyLoss, MSE = (a-b)^2, MAE = |a - b|
                loss = await self.calcMeanSquaredError(y_tensor, y_prediction)
            # step2. loss에 대한 gradient 구하기
            gradients = tape.gradient(loss, [selectedModel.weight, selectedModel.intercept])
            print(f"gradients: {gradients}")
            # step3. gradient update
            # gradient descent 방식으로 모델을 재학습힌다.
            selectedModel.weight.assign_sub(gradients[0] * learningRate)
            selectedModel.intercept.assign_sub(gradients[1] * learningRate)
            # 1 epoch에 대한 gradient descent 끝!


            # 100회 돌때마다 찍어보겠다.
            # 잘하고 있는지 중간점검
            if epoch % 100 == 0:
                print(f"Epoch: {epoch}, Loss {loss.numpy()}")
        # y = wx + b >> 1만번 돌린 최적의 w,b 값을 얻었고 이 상태를 반환
        return selectedModel

    def loadModel(self, wantToBeLoadModel):
        # entity를 구성했기 때문에 이런식으로 가능
        model = LinearRegressionModel() # model : y =wX + b(w, b 안정해진 값)
        # __call__에 의한 self.weight * X + self.intercept의 모델 반환

        # data: w,b(최적의 해로 정해진 값)
        data = np.load(wantToBeLoadModel)

        # 예) 학습으로 얻어진 최적의 w가 2, b가 3이라고 한다면, y = wX + b >> y = 2X + 3
        model.weight.assign(data['weight']) # 최적의 W값 대입
        model.intercept.assign(data['intercept']) # 최적의 b값 대입

        return model

    def predict(self, loadedModel, tensor):
        return loadedModel(tensor).numpy().tolist()
    # 위에 trainModel에서 썼던 list >> numpy >> tensor를 역으로 재생하는 역할
    # 역과정을 하는 이유: 우리가 보기에 list가 좋기 때문




