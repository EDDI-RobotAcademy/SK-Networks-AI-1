from pydantic import BaseModel


class UserPredictRequestForm(BaseModel):
    wannaGetPostText: str
