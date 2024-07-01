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
        # y = 3X + 4, >>> w=3, b=4
        y = 4 + 3 * X + np.random.rand(self.RANGE_MAX,self.RANGE_MIN)

        return X, y

    async def selectLinearRegression(self):
        # 직접적으로 하이퍼파라미터 튜닝을 위해서 라이브러리서 모델 부르는게 아닌 직접 구조 만들어서 불러오기
        return LinearRegressionModel() # 회귀할 때 linear 방식으로 예측하겠다. >> y = wx + b

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
        # tensor화 시키는 이유 : gpu올려서 학습돌리기 위함
        # x =[[], [], []] : type list >> np.array(x) : type np >> tf.constant(x) : type tf.Tensor
        # tf.constant가 np.array를 tf.Tensor로 바꿔주는 기능
        X_tensor = tf.constant(X, dtype=tf.float32) # 학습 데이터
        y_tensor = tf.constant(y, dtype=tf.float32) # 실제 정답

        for epoch in range(numEpochs): # 에포크별로 돌면서 학습
            with tf.GradientTape() as tape:
                y_prediction = selectedModel(X_tensor) # train data X를 y = wx + b >> y pred

                # step1. 매 epcoh마다 loss 구하기
                # 여기서 손실이 최소가 되는 것을 찾는 것임 (변화율 최소)
                # loss 표현에도 여러개가 있는데, crossEntropyLoss, MSE = (a-b)^2, MAE = |a-b|
                loss = await self.calcMeanSquaredError(y_tensor, y_prediction) # 이전에 함수로 다 불러왔던 걸 직접 다 만듦 -> 튜닝을 위함
                print(f"weight : {selectedModel.weight}")
                print(f"loss : {loss}")

                # step2. loss에 대한 gradient 구하기
                # 학습된 내용을 w, b에 적용
                gradients = tape.gradient(loss, [selectedModel.weight, selectedModel.intercept])
                print(f"gradients : {gradients}")

                # step3. gradient update
                # gradient descent 방식으로 모델을 재학습한다. >>
                selectedModel.weight.assign_sub(gradients[0] * learningRate)
                selectedModel.intercept.assign_sub(gradients[1] * learningRate)
                # 1 epcoh에 대한 gradient descent 끝!

            if epoch % 100 == 0: # 100회 때 마다
                print(f"Epoch : {epoch}, Loss: {loss.numpy()}")
        # y = wx + b >> 1만 번 돌린 최적의 w,b 값을 얻었고 이 상태를 반환
        return selectedModel

    def loadModel(self, wantToBeLoadModel):
        # entity를 구성했기 때문에 이런 식으로 가능

        # model : y = wX + b (w, b 안 정해진 값)
        model = LinearRegressionModel() # __call__에 의한 self.weight * x + self.intercept 의 모델 반환

        # data : w,b (최적의 해로 정해진 값)
        data = np.load(wantToBeLoadModel) # data == y = wx + b (w,b train을 통해 얻은 최적값)

        # ex) 학습으로 얻어진 최적의 w가 2, b가 3이라고 한다면,    y = wX + b >> y = 2X + 3
        model.weight.assign(data['weight']) # 최적의 w값 대입
        model.intercept.assign(data['intercept']) # 최적의 b값 대입

        return model

    def predict(self, loadedModel, tensor):
        # 모델 결과(tf.variable?)를 numpy화 시키고 list로 반환
        return loadedModel(tensor).numpy().tolist()