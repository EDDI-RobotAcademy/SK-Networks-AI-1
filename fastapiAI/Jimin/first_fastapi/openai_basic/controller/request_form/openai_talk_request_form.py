from pydantic import BaseModel


class OpenAITalkRequestForm(BaseModel):
    paperTitleList: str