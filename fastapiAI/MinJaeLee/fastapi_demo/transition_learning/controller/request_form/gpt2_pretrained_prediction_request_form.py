from pydantic import BaseModel


class GPT2PretrainedPredictRequestForm(BaseModel):
    text: str
