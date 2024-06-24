import numpy as np
from sklearn.linear_model import LinearRegression

from polynomialRegression.repository.polynomial_regression_repository import PolynomialRegressionRepository

from sklearn.preprocessing import PolynomialFeatures


class PolynomialRegressionRepositoryImpl(PolynomialRegressionRepository):

    def regressionAnalysis(self, X, y):
        print("regressionAnalysis()")

        # 좀 더 엄밀하게 차원 분석을 시켜서 degree 값도 판정하게 해야하나 우선 그냥 진행
        polynomialFeature = PolynomialFeatures(degree=2)
        xPolynomial = polynomialFeature.fit_transform(X)

        model = LinearRegression()
        model.fit(xPolynomial, y)

        X_new = np.linspace(-3, 3, 100).reshape(-1, 1)
        X_new_poly = polynomialFeature.fit_transform(X_new)
        y_pred = model.predict(X_new_poly)

        return X.flatten().tolist(), y.tolist(), X_new.flatten().tolist(), y_pred.tolist()
