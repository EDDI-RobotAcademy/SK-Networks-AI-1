from gradient_descent.repository.gradient_descent_repository import GradientDescentRepository

import numpy as np


class GradientDescentRepositoryImpl(GradientDescentRepository):
    RANGE_MAX = 100
    RANGE_MIN = 1
    RECALL = 42

    def createTrainData(self):
        np.random.seed(self.RECALL)
        X = 2 * np.random.rand(self.RANGE_MAX, self.RANGE_MIN)
        y = 4 + 3 * X + np.random.rand(self.RANGE_MAX, self.RANGE_MIN)

        return X, y
