from sklearn.linear_model import LinearRegression

from exponential_regression.repository.exponential_regression_repository import ExponentialRegressionRepository

import numpy as np


class ExponentialRegressionRepositoryImpl(ExponentialRegressionRepository):

    def regressionAnalysis(self, X, y):
        print("regressionAnalysis()")

        # 지수 회귀 모델 적합을 위해 Log Scale 진행
        # Log 함수 또한 '수학적 선형성' 을 가지고 있음
        # 그럼 '비선형' 은 무엇인가 할 수 있음
        # 예로 온도가 -40 ~ 100도 사이까지는 잘 동작하는 센서가 있다고 가정하겠음
        # 사실 이번에 미국에서 전기 자동차가 다 멈추는 사건이 있었는데
        # 대표적으로 거의 대부분의 모든 반도체들이 위의 온도 범주를 넘어가면 동작을 못함
        # Radiation Hardened 라고 우주 방사선이나 하늘에 떠 있는 비행기 같은 경우에도
        # 좀 더 고려해야 하는 사항들이 존재함
        # 어쨋든 보편적으로 -40 ~ 100도 사이에서는 어떤 특정한 함수를 따르는데
        # 저 범주를 넘어가면 갑자기 이상한 기존과 다른 특성의 함수를 그림
        # 이런 경우 비선형적이라고 함
        # 아직까지 극한의 저온이나
        # 극한의 고온을 버틸 수 없으므로 결국 재료(물질)로 커바치고 있음
        # 결국 엄청 추워지거나 엄청 뜨거워지면 요상한 일이 벌어질지도 ?
        log_y = np.log(y)
        model = LinearRegression()
        model.fit(X[:, np.newaxis], log_y)

        # 이제 로그 스케일을 했으니 실제 예측을 진행
        X_new = np.linspace(1, 100, 100)
        y_pred = np.exp(model.predict(X_new[:, np.newaxis]))

        # 실제 데이터를 반환할 때 이슈가 발생할 수 있는데
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
