from pydantic import BaseModel


class TransitionLearningPredictRequestForm(BaseModel):
    firstSentence: str
    secondSentence: str
