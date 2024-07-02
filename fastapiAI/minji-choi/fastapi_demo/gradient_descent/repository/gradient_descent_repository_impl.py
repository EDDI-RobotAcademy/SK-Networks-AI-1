from sklearn.linear_model import LinearRegression

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

        X = 2 * np.random.rand(self.RANGE_MAX, self.RANGE_MIN)
        y = 4 + 3 * X + np.random.rand(self.RANGE_MAX, self.RANGE_MIN)

        return X, y

    async def selectLinearRegressionModel(self):
        return LinearRegressionModel() # 사이킷런 사용 안함
    async def calcMeanSquaredError(self, y_real, y_prediction):
        return tf.reduce_mean(tf.square(y_real - y_prediction))
    #
    async def trainModel(self, selectedModel, X, y, learningRate=0.01, numEpochs=10000, patience=100):
        X_tensor = tf.constant(X, dtype=tf.float32)
        y_tensor = tf.constant(y, dtype=tf.float32)

        best_loss = float('inf')
        wait = 0

        for epoch in range(numEpochs):
            with tf.GradientTape() as tape:
                y_prediction = selectedModel(X_tensor)
                loss = await self.calcMeanSquaredError(y_tensor, y_prediction)

            gradients = tape.gradient(loss,[selectedModel.weight, selectedModel.intercept])
            selectedModel.weight.assign_sub(gradients[0] * learningRate)
            selectedModel.intercept.assign_sub(gradients[1] * learningRate)

            if epoch % 100 ==0:
                print(f'---- Epoch: {epoch}, Loss: {loss.numpy()} ----')

            # Early stopping 체크
            if loss < best_loss:
                best_loss = loss
                wait = 0
            else:
                wait += 1
                if wait >= patience:
                    print(f"Early stopping at epoch {epoch+1}")
                    break
        return selectedModel

    def loadModel(self, wantToBeLoadModel):
        model = LinearRegressionModel()
        data = np.load(wantToBeLoadModel)
        model.weight.assign(data['weight'])
        model.intercept.assign(data['intercept'])

        return model

    def predict(self, loadedModel, tensor):
        return loadedModel(tensor).numpy().tolist()