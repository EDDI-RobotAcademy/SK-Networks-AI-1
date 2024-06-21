import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from polynomialRegression.repository.polynomial_regression_repository import PolynomialRegressionRepository

class PolynomialRegressionRepositoryImpl(PolynomialRegressionRepository):

    def regressionAnalysis(self, X, y):
        print("regressionAnalysis()")

        # 좀 더 엄밀하게는 차원 분석을 시켜서 degree 값도 판정하게 해야하나 우선 그냥 진행
        # 이전의 X가 [x, x1, 2 ... xn]의 형태였다면
        # 다항 피처 변환 후에는 [1, x1, x2, x1^2, x1^x2 ..] 처럼 다양한 변형이 일어남
        polynomialFeature = PolynomialFeatures(degree=2)
        X_Polynomial = polynomialFeature.fit_transform(X) # X값을 가지고 다항식을 뽑아냄 (모든 x(100개)를 표현할 수 있는 식 반환..)

        # 선형 회귀 분석의 경우 '수학적으로' 선형적인 회귀 분석을 의미함
        # 대표적으로 미,적분은 선형적임
        # x^2, ~ x^4 같은 다항함수도 선형적임
        # 고로 선형 회귀 분석이 적합함
        model = LinearRegression()
        model.fit(X_Polynomial, y) # 모델 학습

        # test data도 미리 만들 수 없나?
        X_new = np.linspace(-3, 3, 100).reshape(-1,1) # -3 ~ 3 사이의 100개값 뽑기
        X_new_poly = polynomialFeature.transform(X_new) # X_new로 다항식 뽑기 >> test data X
        y_pred = model.predict(X_new_poly) # test 데이터로 모델에 넣어 예측값 얻기

        # flatten이 1행 n열로 되어있는걸 => n행 1열로 바꾸는 작업인가?
        return X.flatten().tolist(), y.tolist(), X_new.flatten().tolist(), y_pred.tolist()
