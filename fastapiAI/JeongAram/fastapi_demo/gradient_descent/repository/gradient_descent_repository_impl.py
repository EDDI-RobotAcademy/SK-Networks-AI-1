

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
        X = 2 * np.random.rand(self.RANGE_MAX, self.RANGE_MIN) # RANGE_MAX 행, RANGE_MIN 열의 random matrix 생성
        # 가우시간 분포 2 -> 서로 종속관계
        # y = 3X + 4 -> w = 3, b = 4
        y = 4 + 3 * X + np.random.rand(self.RANGE_MAX, self.RANGE_MIN)

        return X, y

    async def selectLinearRegressionModel(self):
        return LinearRegressionModel()

    async def calcMeanSquaredError(self, y_real, y_prediction):
        return tf.reduce_mean(tf.square(y_real - y_prediction))

    async def trainModel(self, selectedModel, X, y, learningRate=0.01, numEpochs=10000):
        # tensor화 시키는 이유: gpu 올려서 학습 돌리기 위함
        # x = [[], [], []] : type list -> np.array(x) : type np -> tf.constant(x) : type tf.Tensor
        # 타입마다 사용할 수 있는 것이 다르다.
        # tf.constant가 np.arrray를 tf.Tensor로 바꿔주는 기능
        X_tensor = tf.constant(X, dtype=tf.float32) # 학습 데이터
        y_tensor = tf.constant(y, dtype=tf.float32) # 실제 정답

        # print(f"selectedModel: {selectedModel}")

        for epoch in range(numEpochs):
            with tf.GradientTape() as tape:
                y_prediction = selectedModel(X_tensor)
                # print(f"y_prediction: {y_prediction}")
                # step1. 매 epoch마다 loss 구하기
                # 여기서 손실이 최소가 되는 것을 찾는 것임(변화율 최소)
                # loss 표현에도 여러개가 있는데, crossEntropyLoss, MSE = (a-b)^2, MAE = |a-b|
                loss = await self.calcMeanSquaredError(y_tensor, y_prediction)

            # step2. loss에 대한 gradient 구하기
            # loss를 재학습 시켜야하는데 그 방식이 gradient descent임 -> 기울기를 알아야 함
            gradients = tape.gradient(loss, [selectedModel.weight, selectedModel.intercept])
            print(f"gradients: {gradients}")

            # step3. gradient update
            # gradient descent 방식으로 모델을 재학습한다.
            selectedModel.weight.assign_sub(gradients[0] * learningRate)
            selectedModel.intercept.assign_sub(gradients[1] * learningRate)
            # 1 epoch에 대한 gradient descent 끝!

            # 100회 때 마다 -> 중간중간 잘 되고 있는지 확인을 위해서
            if epoch % 100 == 0:
                print(f"Epoch: {epoch}, Loss: {loss.numpy()}")
        # y = wx + b -> 1만 번 돌린 최적의 w, b 값을 얻었고 이 상태를 반환
        return selectedModel

    def loadModel(self, wantToBeLoadModel):
        # entity를 구성했기 때문에 이런 식으로 가능

        # model = wX + b (w, b는 안 정해진 값)
        model = LinearRegressionModel() # __call__에 의한 self.weight * X + self.intercept 의 모델 반환

        # data : w, b(최적의 해로 정해진 값)
        data = np.load(wantToBeLoadModel) # 올리고 싶은 모델, data == y = wx + b(w, b train을 통해 얻은 최적값)

        # ex) 학습으로 얻어진 최적의 w가 2, b가 3이라고 한다면 y = wX + b -> y = 2X + 3
        model.weight.assign(data['weight']) # 최적의 w값 대입
        model.intercept.assign(data['intercept']) # 최적의 b값 대입

        return model

    def predict(self, loadedModel, tensor):
        # 결과를(tensor) numpy화 시키고 list로 반환 -> 우리가 보고 이용하기 위해서 다시 역과정
        # tensor는 gpu를 위한 것이라고 생각하면 될 듯
        return loadedModel(tensor).numpy().tolist()


