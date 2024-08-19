from pydantic import BaseModel


class SentimentAnalysisRequestForm(BaseModel):
    sentence: str
