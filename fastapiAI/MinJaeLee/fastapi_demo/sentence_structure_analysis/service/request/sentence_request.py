from pydantic import BaseModel


class SentenceRequest(BaseModel):
    sentence: str

    def toSentence(self):
        return self.sentence
