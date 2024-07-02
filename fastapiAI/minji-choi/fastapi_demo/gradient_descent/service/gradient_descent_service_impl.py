from gradient_descent.repository.gradient_descent_repository_impl import GradientDescentRepositoryImpl
from gradient_descent.service.gradient_descent_service import GradientDescentService
import numpy as np
import os
class GradientDescentServiceImpl(GradientDescentService):
    SAVED_MODEL_PATH = 'linear_regression_model.npz'
    def __init__(self):
        self.gradientDescentRepository = GradientDescentRepositoryImpl()
    def saveTrainedModel(self, trainedModel, path):
        np.savez(path, weight=trainedModel.weight.numpy(), intercept=trainedModel.intercept.numpy())
        print(f'model saved at {os.path.join(os.getcwd(),path)}')

    async def gradientDescentTrain(self):
        print('service -> gradientDescentTrain()')

        X, y = await self.gradientDescentRepository.createTrainData()
        selectedModel = await self.gradientDescentRepository.selectLinearRegressionModel()
        trainedModel = await self.gradientDescentRepository.trainModel(selectedModel, X, y)


        self.saveTrainedModel(trainedModel, self.SAVED_MODEL_PATH)
        return True

    async def gradientDescentPredict(self, request):
        if (self.checkValidation() == False) :
            return {"error": "모델 학습부터 실행하세요"}
        print('학습이 완료된 상태')
        loadedModel = self.gradientDescentRepository.loadModel(self.SAVED_MODEL_PATH)
        predictions = self.gradientDescentRepository.predict(loadedModel, request.toTensor())
        return predictions

    def checkValidation(self):
        if not os.path.exists('linear_regression_model.npz'):
            return False
        return True