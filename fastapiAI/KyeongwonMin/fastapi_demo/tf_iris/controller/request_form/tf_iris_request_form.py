from pydantic import BaseModel


class TfIrisRequestForm(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
