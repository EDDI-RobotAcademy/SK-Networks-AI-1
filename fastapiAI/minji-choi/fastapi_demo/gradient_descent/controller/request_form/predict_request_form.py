from typing import List

from pydantic import BaseModel
from gradient_descent.service.request.predict_request import PredictRequest


class PredictRequestForm(BaseModel):
    X:list

    # requestForm을 request로 바꿔주는 작업
    def toPredictRequest(self) -> PredictRequest:
        return PredictRequest(X=self.X)