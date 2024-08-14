from pydantic import BaseModel

class SequenceAnalysisRequestForm(BaseModel):
    userSendMessage: str