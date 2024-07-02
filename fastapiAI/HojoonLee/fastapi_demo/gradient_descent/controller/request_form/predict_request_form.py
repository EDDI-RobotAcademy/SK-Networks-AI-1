from pydantic import BaseModel
from gradient_descent.service.request.predict_request import PredictRequest

class PredictRequestForm(BaseModel):
    # BaseModel할 때는 생성자를 만들거나 파라미터를 넣으면 안됨
    X: list

    def toPredictRequest(self) -> PredictRequest:
        return PredictRequest(X=self.X)