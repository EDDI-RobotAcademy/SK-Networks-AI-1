from pydantic import BaseModel

from sentence_structure_analysis.service.request.sentence_request import SentenceRequest

class SentenceRequestForm(BaseModel):
    sentence: str

    # return type은 service에 있는 request
    # SentenceRequestForm -> SentenceRequest로 포장지 까기
    def toSentenceRequest(self) -> SentenceRequest:
        return SentenceRequest(sentence=self.sentence)