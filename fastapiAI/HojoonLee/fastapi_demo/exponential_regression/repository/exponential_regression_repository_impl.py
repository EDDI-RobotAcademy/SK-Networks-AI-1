import numpy as np

from exponential_regression.repository.exponential_regression_repository import ExponentialRegressionRepository
from sklearn.linear_model import LinearRegression
class ExponentialRegressionRepositoryImpl(ExponentialRegressionRepository):

    def regressionAnalysis(self, X, y):

        print("regressionAnalysis()")
        # 데이터 repository까지 잘 받아와졌으니 이걸로 계산하기
        # print(f"X: {X}")
        # print(f"y: {y}")

        # 지수 회귀 모델 적합을 위해 Log Scale 진행
        # log 함수 또한 '수학적 선형성'을 가지고 있음
        # 비선형의 예는 무엇인가?
        # 대표적으로 거의 대부분의 반도체들이 온도 범주를 넘어가면 동작을 못함
        log_y = np.log(y)
        model = LinearRegression()
        model.fit(X[:, np.newaxis], log_y) # 행렬 연산 위해 X는 transpose

        # 로그 스케일링 했으니 실제 예측 진행 test !
        X_new = np.linspace(1, 100, 100) # test data
        y_pred = np.exp(model.predict(X_new[:, np.newaxis])) # log 스케일링 햇으니 다시 exp해서 y반환

        # 실제 데이터를 반환할 때 이슈가 발생할 수 있는데
        # 지금 numpy를 쓰기 때문에 데이터 타입이 numpy Type에 해당함
        # 이것을 적절하게 바꿔줘야함 json 형식으로
        result = {
            "original_data": list(map(lambda x: [int(x[0]), float(x[1])],zip(X, y))),
            "predicted_data": list(map(lambda x: [float(x[0]), float(x[1])], zip(X_new, y_pred))),
            "coefficent": model.coef_.tolist(),
            "intercept": float(model.intercept_)
        }
        return result