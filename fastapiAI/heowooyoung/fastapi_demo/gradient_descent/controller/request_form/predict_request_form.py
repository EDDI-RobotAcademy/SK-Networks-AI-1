from pydantic import BaseModel

from gradient_descent.service.request.predict_request import PredictRequest


class PredictRequestForm(BaseModel):
    X: list

    def toPredictRequest(self) -> PredictRequest:
        return PredictRequest(X=self.X)