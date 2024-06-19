import numpy as np
from sklearn.linear_model import LinearRegression

from polynomialRegression.repository.polynomial_regression_repository import PolynomialRegressionRepository
from sklearn.preprocessing import PolynomialFeatures

class PolynomialRegressionRepositoryImpl(PolynomialRegressionRepository):

    def regressionAnalysis(self, X, y):
        print("regressionAnalysis()")

        # 좀 더 엄밀하게는 차원 분석을 시켜서 degree 값도 판정하게 해야하나 우산 그냥 진행
        # 다항 형식의 Feature 추출
        polynomialFeature = PolynomialFeatures(degree=2)
        X_Polynomial = polynomialFeature.fit_transform(X)
        
        # 선형 회귀 분석의 경우 '수학적'으로 '선형'적인 회귀 분석을 의미함
        # 대표적으로 적분이나 미분은 '선형적'임
        # x^2, x^3, x^4 같은 다항 함수도 '선형적'임
        # 고로 선형 회귀 분석이 적합함
        model = LinearRegression()
        # fit을 통해 위와 같은 데이터를 학습시킴
        model.fit(X_Polynomial, y)

        # -3 ~ 3 사이를 100개의 균일한 값으로 구성하고 100행 1열로 변환
        X_new = np.linspace(-3, 3, 100).reshape(-1, 1)
        # 새로 뽑은 X_new를 다항 피처로 변환함 [ 1, x1, x2, x1^2, x1 * x2, x^2, ... ]
        X_new_poly = polynomialFeature.transform(X_new)
        # 각 다항 피처에 대한 y 값 예측
        y_pred = model.predict(X_new_poly)

        # flatten()이 붙은 케이스들은 전부 1차원 형태로 만들고 리스트화하여 반환
        return X.flatten().tolist(), y.tolist(), X_new.flatten().tolist(), y_pred.tolist()
        