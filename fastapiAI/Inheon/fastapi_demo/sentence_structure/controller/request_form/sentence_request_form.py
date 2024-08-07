from pydantic import BaseModel

from sentence_structure.service.request.sentence_request import SentenceRequest


class SentenceRequestForm(BaseModel):
    sentence: str

    def toSentenceRequest(self) -> SentenceRequest:
        return SentenceRequest(sentence=self.sentence)