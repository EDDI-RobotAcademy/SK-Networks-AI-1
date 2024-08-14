from pydantic import BaseModel

class SrbcbRequestForm(BaseModel):
    userSendMessage: str