from pydantic import BaseModel


class UserPredictRequestForm(BaseModel):
    wannaGetPostText: str

    def getWannaGetPostText(self):
        return self.wannaGetPostText
