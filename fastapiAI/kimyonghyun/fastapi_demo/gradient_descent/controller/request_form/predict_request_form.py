from pydantic import BaseModel

from gradient_descent.service.request.predict_request import PredictRequest
import tensorflow as tf


class PredictRequestForm(BaseModel):
    X: list

    def toPredictRequest(self) -> PredictRequest:
        print(f"X: {self.X}")
        return PredictRequest(self.X)