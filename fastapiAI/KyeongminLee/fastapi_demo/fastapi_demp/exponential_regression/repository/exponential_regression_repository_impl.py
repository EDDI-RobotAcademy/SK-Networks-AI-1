import numpy as np
from sklearn.linear_model import LinearRegression

from exponential_regression.repository.exponential_regression_repository import ExponentialRegressionRepository


class ExponentialRegressionRepositoryImpl(ExponentialRegressionRepository):
    def regressionAnalysis(self, X, y):
        print("regressionAnalysis()")

        # 지수 회귀 모델 적합을 위해 Log Scale 진행
        log_y = np.log(y)
        model = LinearRegression()
        model.fit(X[:, np.newaxis], log_y)

        # 로그 스케일 후, 실제 예측 진행
        X_new = np.linspace(1, 100, 100)
        y_pred = np.exp(model.predict(X_new[:, np.newaxis]))

        # 실제 데이터를 반환할 때 이슈 발생할 수 있는데,
        # 지금 numpy를 쓰고 있기 때문에 데이터 타입이 Numpy Type에 해당함
        # 이것을 적절하게 변환해줘야함
        result = {
            "original_data": list(
                map(lambda x: [
                    int(x[0]), float(x[1])
                ], zip(X, y))),
            "predicted_data": list(
                map(lambda x: [
                    float(x[0]), float(x[1])
                ], zip(X_new, y_pred))),
            "coefficient": model.coef_.tolist(),
            "intercept": float(model.intercept_)
        }

        return result