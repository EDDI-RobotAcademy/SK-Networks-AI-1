from pydantic import BaseModel

from sentence_structure_analysis.service.request.sentence_structure_analysis_request import SentenceRequest


class SentenceRequestForm(BaseModel):
    sentence: str

    def toSentenceRequest(self) -> SentenceRequest:
        return SentenceRequest(sentence=self.sentence)