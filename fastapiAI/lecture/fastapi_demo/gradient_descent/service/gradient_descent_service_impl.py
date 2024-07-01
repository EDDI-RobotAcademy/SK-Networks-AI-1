from gradient_descent.repository.gradient_descent_repository_impl import GradientDescentRepositoryImpl
from gradient_descent.service.gradient_descent_service import GradientDescentService


class GradientDescentServiceImpl(GradientDescentService):

    def __init__(self):
        self.gradientDescentRepository = GradientDescentRepositoryImpl()

    def gradientDescentTrain(self):
        print("service -> gradientDescentTrain()")

        X, y = self.gradientDescentRepository.createTrainData()
        print(f"X: {X}")
        print(f"y: {y}")


