from gradient_descent.entity.linear_regression_model import LinearRegressionModel
from gradient_descent.repository.gradient_descent_repository import GradientDescentRepository
import numpy as np
import tensorflow as tf

class GradientDescentRepositoryImpl(GradientDescentRepository):
    RANGE_MAX = 100
    RANGE_MIN = 1
    RECALL = 42

    def createTrainData(self):
        print("repository -> createTrainData()")
        np.random.seed(self.RECALL)
        X = 2 * np.random.rand(self.RANGE_MAX, self.RANGE_MIN) # RANGE_MAX 행, RANGE_MIN 열의 random matrix 생성
        y = 4 + 3 * X + np.random.rand(self.RANGE_MAX,self.RANGE_MIN)

        return X, y

    async def selectLinearRegression(self):
        # 직접적으로 하이퍼파라미터 튜닝을 위해서 라이브러리서 모델 부르는게 아닌 직접 구조 만들어서 불러오기
        return LinearRegressionModel()

    async def calcMeanSquaredError(self, y_real, y_pred):
        # 최소제곱오차 (둘의 차이를 제곱 씌운 평균을 반환 >> 텐서이므로 여러개의 값이 존재)
        return tf.reduce_mean(tf.square(y_real - y_pred))

    # Gradient Descnet는 변화율이 최소가 되는 최적 경로를 찾기 위해 사용하는 편임
    # 그렇기 때문에 위와 같은 MSE 계산이 진행됨
    # 좀 더 수식적으로 표현하면 origin - learningRate * delta(origin_pred) 라고 볼 수 있음
    # delta : 벡터의 도함수로 단순히 d/dt의 형태가 아님
    # 벡터이기 때문에 미분 연산자 자체가 Curl, Divergence, Gradient 3가지 형태로 나뉨
    # 그 중 Gradient가 2차원에서 다뤘던 기울기 d/dt와 유사함
    # 고로 사실상 쉽게 생각하면 (현재 값 - 이전 값 / 시간) 느낌으로 해석이 가능함
    async def trainModel(self, selectedModel, X, y, learningRate=0.01, numEpochs=10000):
        X_tensor = tf.constant(X, dtype=tf.float32) # 학습 데이터
        y_tensor = tf.constant(y, dtype=tf.float32) # 실제 정답

        for epoch in range(numEpochs): # 에포크별로 돌면서 학습
            with tf.GradientTape() as tape:
                y_prediction = selectedModel(X_tensor)
                # 여기서 손실이 최소가 되는 것을 찾는 것임 (변화율 최소)
                loss = await self.calcMeanSquaredError(y_tensor, y_prediction) # 이전에 함수로 다 불러왔던 걸 직접 다 만듦 -> 튜닝을 위함
                print(f"weight : {selectedModel.weight}")
                print(f"loss : {loss}")
                # 학습된 내용을 w, b에 적용
                gradients = tape.gradient(loss, [selectedModel.weight, selectedModel.intercept])
                print(f"gradients : {gradients}")
                selectedModel.weight.assign_sub(gradients[0] * learningRate)
                selectedModel.intercept.assign_sub(gradients[1] * learningRate)

            if epoch % 100 == 0: # 100회 때 마다
                print(f"Epoch : {epoch}, Loss: {loss.numpy()}")

        return selectedModel

    def loadModel(self, wantToBeLoadModel):
        # entity를 구성했기 때문에 이런 식으로 가능
        model = LinearRegressionModel() # __call__에 의한 self.weight * x + self.intercept 의 모델 반환
        data = np.load(wantToBeLoadModel) # 올리고싶은 모델
        model.weight.assign(data['weight'])
        model.intercept.assign(data['intercept'])

        return model

    def predict(self, loadedModel, tensor):
        # 모델 결과(tf.variable?)를 numpy화 시키고 list로 반환
        return loadedModel(tensor).numpy().tolist()