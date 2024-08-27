from pydantic import BaseModel

class Gpt2PretrainedPredictionRequestForm(BaseModel):
    text: str