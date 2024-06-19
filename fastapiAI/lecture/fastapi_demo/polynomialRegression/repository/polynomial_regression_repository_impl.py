import numpy as np
from sklearn.linear_model import LinearRegression

from polynomialRegression.repository.polynomial_regression_repository import PolynomialRegressionRepository

from sklearn.preprocessing import PolynomialFeatures


class PolynomialRegressionRepositoryImpl(PolynomialRegressionRepository):

    def regressionAnalysis(self, X, y):
        print("regressionAnalysis()")

        # 좀 더 엄밀하게는 차원 분석을 시켜서 degree 값도 판정하게 해야하나 우선 그냥 진행
        # 다항 형식의 Feature 추출
        # 이 녀석의 특징이라면 X가 [x1, x2, x3, ..., x_n] 이라면
        # 다항 피쳐 변환 후에는 [1, x1, x2, x1^2, x1 * x2, x^2, ... ] 과 같은 형태를 가지게 됨

        # Q. 선형 회귀는 y = x 형태고, 다항 회귀는 100개축이 있으면 100차원인지 ?
        # A. 우선 기저(축)이 100개 있으면 100차원이 맞습니다.
        #    그런데 우리는 degree=2 를 줬기 때문에 2차 함수에 대한 분석이라 보면 되겠습니다.
        #    degree=3 이면 3차 함수, 4면 4차 함수라 보면 되겠습니다.
        #    여기서 이제 조금 더 나가면 x, y, z가 물리는 경우가 발생할 수 있는데
        #    이런 복잡한 영역은 선형 회귀가 불가합니다 (왜냐하면 비선형적이기 때문입니다)
        #    보편적으로 화학 분석, 재료 분석 같은 것을 할 때 많이 사용합니다.
        #    예로 배터리 만들 때 보면 A랑 B랑 1:1로 섞으면 뭐가 된다 합니다.
        #    근데 막상 대용량으로 만들기 시작하면 1:1 비율이 틀어지게 됩니다.
        #    (이런 것이 대표적인 비선형적인 문제인데 <- 논문 쓰기엔 좋지만 이걸로 문제 해결이 안됨)
        #    사실 이건 인간이 노가다로 비율 맞춰야합니다 ;;;
        #    결론이 비선형 문제는 살짝 비현실적 허상 같은 느낌이 있습니다.
        #    -> 학교에서 편미분 방정식을 배우면 재밌는 사례가 있는데
        #       경계 조건이 딱딱 들어맞으면 아주 나이스하게 풀 수 있습니다.
        #    -> 그러나 현실 문제에서는 저런게 없어요.
        #    결론: 노가다 만세
        polynomialFeature = PolynomialFeatures(degree=2)
        X_Polynomial = polynomialFeature.fit_transform(X)
        # print(f"X_Polynomial: {X_Polynomial}")

        # 선형 회귀 분석의 경우 '수학적'으로 '선형'적인 회귀 분석을 의미함
        # 대표적으로 적분이나 미분은 '선형적'임
        # x^2, x^3, x^4 같은 다항 함수도 '선형적'임
        # 고로 선형 회귀 분석이 적합함
        model = LinearRegression()
        # fit을 통해 위와 같은 데이터를 학습시킴
        model.fit(X_Polynomial, y)

        # 결론: ax^2 + bx + cx + d를 예측했다 보면 됨
        # -3 ~ 3 사이를 100개의 균일한 값으로 구성하고 100행 1열로 변환
        X_new = np.linspace(-3, 3, 100).reshape(-1, 1)
        # 새로 뽑은 X_new를 다항 피처로 변환함 [1, x1, x2, x1^2, x1 * x2, x^2, ... ]
        X_new_poly = polynomialFeature.transform(X_new)
        # 각 다항 피처에 대한 y 값 예측
        y_pred = model.predict(X_new_poly)

        # flatten()이 붙은 케이스들은 전부 1차원 형태로 만들고 리스트화하여 반환
        return X.flatten().tolist(), y.tolist(), X_new.flatten().tolist(), y_pred.tolist()
