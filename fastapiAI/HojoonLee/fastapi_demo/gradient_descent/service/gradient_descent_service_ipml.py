import os

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

        X, y = self.gradientDescentRepository.createTrainData() # 학습 데이터 생성

        # model selection
        selectedModel = await self.gradientDescentRepository.selectLinearRegression() # 모델 선택

        # print(f"type check : {type(selectedModel)}")
        # type check : <class 'gradient_descent.entity.linear_regression_model.LinearRegressionModel'>

        # y = wx + b 모델에 X,y
        trainedModel = await self.gradientDescentRepository.trainModel(selectedModel, X, y) # 선택된 모델로 학습

        self.saveTrainedModel(trainedModel, self.SAVED_MODEL_PATH)

        return True

    def checkValidation(self):
        if not os.path.exists(self.SAVED_MODEL_PATH):
            return False
        return True


    async def gradientDescentPredict(self, request):
        if (self.checkValidation() == False):
            return {"error": "모델부터 학습시키세요!"}

        loadedModel = self.gradientDescentRepository.loadModel(self.SAVED_MODEL_PATH)

        # prediction
        # predict request에 있는 toTensor() 함수를 통해 request를 tensor화 시킨다.
        # 예측(잘 학습시켰던 모델, 테스트 입력 데이터)
        predictions = self.gradientDescentRepository.predict(loadedModel, request.toTensor())

        return predictions

