from pydantic import BaseModel


class GDFTUserRequestForm(BaseModel):
    text: str
