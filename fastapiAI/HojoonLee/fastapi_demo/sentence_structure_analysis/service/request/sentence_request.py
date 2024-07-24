from pydantic import BaseModel

class SentenceRequest(BaseModel):
    sentence: str

    # sentenceRequest 이란 포장지에서 포장지 벗긴 내용물 sentence 반환
    # sentenceRequest -> sentence (text)
    def toSentence(self):
        return self.sentence