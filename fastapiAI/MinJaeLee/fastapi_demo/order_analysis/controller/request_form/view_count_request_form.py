from pydantic import BaseModel


class ViewCountRequestForm(BaseModel):
    count:int