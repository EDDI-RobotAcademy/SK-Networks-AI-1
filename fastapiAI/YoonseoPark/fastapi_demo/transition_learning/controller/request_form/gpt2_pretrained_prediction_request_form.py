from pydantic import BaseModel


class GPT2PretrainedPredictionRequestForm(BaseModel):
    text: str