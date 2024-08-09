from pydantic import BaseModel


class UserReviewRequestForm(BaseModel):
    userInputText: str

    def getUserInputText(self):
        return self.userInputText
