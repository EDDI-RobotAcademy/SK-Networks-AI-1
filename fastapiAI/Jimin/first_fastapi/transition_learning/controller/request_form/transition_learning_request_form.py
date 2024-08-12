from pydantic import BaseModel


class TransitionLearningRequestForm(BaseModel):
    firstSentence : str
    secondSentence: str