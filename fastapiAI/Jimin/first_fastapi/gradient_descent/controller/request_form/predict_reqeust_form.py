from pydantic import BaseModel
import tensorflow as tf

from gradient_descent.service.request.predict_request import PredictRequest

# BaseModel 사용시 생성자를 만들거나 parameter를 만들면 안된다.
class PredictRequestForm(BaseModel):
    X: list

    def toPredictReqeust(self) -> PredictRequest:
        return PredictRequest(X=self.X)

    # requestform이 복잡히 올 수가 있다.
    # 각 도메인별로 구성해서 날아갈 수 있도록 해주는게 toPredictRequest이다.