from gradient_descent.entity.linear_regression_model import LinearRegressionModel
from gradient_descent.repository.gradient_descent_repository import GradientDescentRepository

import tensorflow as tf
import numpy as np


class GradientDescentRepositoryImpl(GradientDescentRepository):
    RANGE_MAX = 100
    RANGE_MIN = 1
    RECALL = 42

    async def createTrainData(self):    # 딥러닝에서 제일 중요한게 이 부분(노이즈 값을 어떻게 최소화할 것이냐)임
        # np화 시킴
        np.random.seed(self.RECALL)     # 노이즈값을 넣은 거임???????????????
        X = 2 * np.random.rand(self.RANGE_MAX, self.RANGE_MIN)      # 정규분포(가우시안분포)1
        # y = 3X + 4
        y = 4 + 3 * X + np.random.rand(self.RANGE_MAX, self.RANGE_MIN)   # 정규분포(가우시안분포)2

        return X, y

    async def selectLinearRegressionModel(self):
        return LinearRegressionModel()  # 회귀할 때 Linear방식으로 예측하겠다.

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
        # tensor는 자료형의 하나임.
        # x = [[],[],[]] : type list -> np.array : type np -> tf.constant(x) : typr tf.tensor
        # tensor화 시키는 이유 : gpu에 올려서 학습돌리기 위함
        # tf.constant가 np.array를 tf.tensor로 바꿔주는 기능 -> 즉, 그냥 np.array 상태면 gpu에 올릴 수 없으니 tf.constant를 통해 tf.tensor로 바꾸어서 gpu에 올릴 수 있는 상태로 변경해주는 것.
        X_tensor = tf.constant(X, dtype=tf.float32)     # 학습 데이터
        y_tensor = tf.constant(y, dtype=tf.float32)     # 실제 정답

        print(f"selectedModel: {selectedModel}")

        for epoch in range(numEpoches):     # epoch별로 돌면서 학습
            with tf.GradientTape() as tape:
                y_prediction = selectedModel(X_tensor)      #train data X를 y = wx + b -> y pred

                # step1. 매 epoch마다 loss구하기
                # 여기서 손실이 최소가 되는 것을 찾는 것임 (변화율 최소)
                # loss 표현에도 여러개가 있는데 crossEntropyLoss, MSE = (a-b)^2, MAE = |a-b|
                loss = await self.calcMeanSquaredError(y_tensor, y_prediction)

            print(f"loss: {loss}")
            print(f"weight: {selectedModel.weight}")
            print(f"intercept: {selectedModel.intercept}")

            # step2. loss에 대한 gradients 구하기
            # 학습된 내용을 w,b에 적용
            gradients = tape.gradient(loss, [selectedModel.weight, selectedModel.intercept])
            print(f"gradients: {gradients}")

            # step3. gradients 업데이트
            # gradients Descent방식으로 모델을 재학습한다.
            selectedModel.weight.assign_sub(gradients[0] * learningRate)
            selectedModel.intercept.assign_sub(gradients[1] * learningRate)
            # ------------ 여기까지가 1 epoch에 대한 gradients Descent  끝


            if epoch % 100 == 0:  # 100회마다
                print(f"Epoch: {epoch}, Loss: {loss.numpy()}")

        #y = wx + b -> 10000번 돌린 최적의 w,b값을 얻었고 이 상태를 반환함.
        return selectedModel


    def loadModel(self, wantToBeLoadModel):

        # entity를 구성했기 때문에 이런 식으로 가능

        # model : y = wX + b (w, b가 안 정해진 값)
        model = LinearRegressionModel()        # __call__에 의한 self.weight * x + self.intercept의 모델 변환 질문 -> entity화 시켰다는게 무슨 뜻?

        # data: w, b(최적의 해로 정해진 값)
        data = np.load(wantToBeLoadModel)       # 올리고 싶은 모델, data == y = wx + b (w,b train을 통해 얻은 최적값)

        # ex) 학습으로 없어진 최적의 w가 2, b가 3이라고 한다면, y=wX+b -> y=2X+3
        model.weight.assign(data['weight'])     # 최적의 w값 대입
        model.intercept.assign(data['intercept'])      # 최적의 b값 대입

                                        # w,b를 구하는 이유는 어떠한 값이 들어와도 loss가 가장 적은 최적의 값을 구하기 위해. (즉, 어떤 값이 들어와도 설명할 수 있는? 값을 찾기 위해)
        return model

    def predict(self, loadedModel, tensor):
        #모델 결과(tf.variable)를 numpy화 시키고 list로 반환
        return loadedModel(tensor).numpy().tolist()     # 학습을 돌릴떈 리스트 -> 넘파이화 -> 텐서화를 시켰어야 하는데 이젠 우리가 봐야하므로 역과정을 진행 즉, 텐서->넘파이->리스트화를 시켜준 것임.