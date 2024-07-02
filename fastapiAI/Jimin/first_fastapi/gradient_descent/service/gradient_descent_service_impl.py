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


    # 유효성 검사
    # requestform에서 포장지 뜯었기 때문에 request이다.
    # 참고로 controller코드에서 request 포장뜯는 코드 있음.
    async def gradientDescentPredict(self, request):
        if (self.checkValidation() == False):
            return {"eror": "모델 학습부터 시키세요"}

        print("학습이 잘 되어있는 상태입니다")

        loadedModel = self.gradientDescentRepository.loadModel(self.SAVED_MODEL_PATH)

        # 리스트인 상황에서는 predict나 train(곧 gpu 연산)이 안된다.
        # 따라서 tensor로 바꿔준다.
        # 우리 수준에서 뭘 하려고 하면 (이미지 rgb 값바꾸기등등) numpy
        # gpu로 올려서 연산할 때는 tensor
        # 예측(잘 학습시켰던 모델, 테스트 입력 데이터)
        predictions = self.gradientDescentRepository.predict(loadedModel, request.toTensor())
        # 입력(X)을 줬을 때 최적의 W, b를 리턴한다.
        return predictions





