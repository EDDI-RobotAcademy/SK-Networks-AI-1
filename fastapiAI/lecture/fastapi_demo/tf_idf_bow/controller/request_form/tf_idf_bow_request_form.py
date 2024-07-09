from pydantic import BaseModel


class TfIdfBowRequestForm(BaseModel):
    userSendMessage: str
