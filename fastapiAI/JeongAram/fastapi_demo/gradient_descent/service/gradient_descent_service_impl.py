import os.path

from gradient_descent.repository.gradient_descent_repository_impl import GradientDescentRepositoryImpl
from gradient_descent.service.gradient_descent_service import GradientDescentService
import numpy as np

class GradientDescentServiceImpl(GradientDescentService):
    SAVED_MODEL_PATH = 'linear_regression_model.npz'

    def __init__(self):
        self.gradientDescentRepository = GradientDescentRepositoryImpl()

    def saveTrainedModel(self, trainedModel, path):
        np.savez(path, weight=trainedModel.weight.numpy(), intercept=trainedModel.intercept.numpy())

    async def gradientDescentTrain(self):
        print("service -> gradientDescentTrain()")

        X, y = await self.gradientDescentRepository.createTrainData()
        # print(f"X: {X}")
        # print(f"y: {y}")

        selectedModel = await self.gradientDescentRepository.selectLinearRegressionModel()
        # print(f"type check: {type(selectedModel)}")

        trainedModel = await self.gradientDescentRepository.trainModel(selectedModel, X, y)

        self.saveTrainedModel(trainedModel, self.SAVED_MODEL_PATH)

        return True

    def checkValidation(self):
        if not os.path.exists(self.SAVED_MODEL_PATH):
            return False

        return True

    async def gradientDescentPredict(self, request):
        if (self.checkValidation() == False):
            return {"error": "모델 학습부터 시키세요!"}

        print("학습이 잘 되어있는 상태입니다!")

        loadedModel = self.gradientDescentRepository.loadModel(self.SAVED_MODEL_PATH)

        # predict request에 있는 toTensor() 함수를 통해 request를 tensor화 시킨다.
        # 예측(잘 학습시켰던 모델, 테스트 입력 데이터)
        predictions = self.gradientDescentRepository.predict(loadedModel, request.toTensor())

        # X와 y를 입력했을 때 최적의 w, b를 예측해준다.
        return predictions

        # X_new = tf.constant(request.X, dtype=tf.float32)
        # predictions = model(X_new).numpy().tolist()






