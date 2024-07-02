import numpy as np
from sklearn.linear_model import LinearRegression
from polynomialRegression.repository.polynomial_regression_repository import PolynomialRegressionRepository
from sklearn.preprocessing import PolynomialFeatures

class PolynomialRegressionRepositoryImpl(PolynomialRegressionRepository):

    def regressionAnalysis(self, X, y):
        print('regressionAnalysis()')
        polynomialFeature = PolynomialFeatures(degree=2)

        X_Polynomial = polynomialFeature.fit_transform(X)

        model = LinearRegression()
        model.fit(X_Polynomial, y)

        X_new = np.linspace(-3, 3, 100).reshape(-1,1)
        X_new_poly = polynomialFeature.transform(X_new)
        y_pred = model.predict(X_new_poly)
        return X.flatten().tolist(), y.tolist(), X_new.flatten().tolist(), y_pred.tolist()