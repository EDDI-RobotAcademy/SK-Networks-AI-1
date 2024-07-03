import os

from gradient_descent.repository.gradient_descent_repository_impl import GradientDescentRepositoryImpl
from gradient_descent.service.gradient_descent_service import GradientDescentService

import numpy as np

from gradient_descent.service.request.predict_request import PredictRequest


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
        if self.checkValidation() == False:
            return {"error": "모델 학습이 필요합니다."}

        print("학습이 잘 되어 있는 상태입니다.")
        loadedModel = self.gradientDescentRepository.loadModel(self.SAVED_MODEL_PATH)

        predictions = self.gradientDescentRepository.predict(loadedModel, request.toTensor())

        return predictions