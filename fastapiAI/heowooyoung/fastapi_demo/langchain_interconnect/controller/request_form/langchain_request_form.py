from pydantic import BaseModel

class LangchainRequestForm(BaseModel):
    userSendMessage: str