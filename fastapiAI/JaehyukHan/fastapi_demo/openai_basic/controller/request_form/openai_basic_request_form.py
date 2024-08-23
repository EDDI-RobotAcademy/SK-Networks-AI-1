from pydantic import BaseModel


class OpenAITalkRequestForm(BaseModel):
    userSendMessage: str
