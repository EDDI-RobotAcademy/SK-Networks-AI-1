from pydantic import BaseModel


class Post(BaseModel):
    id: int = None
    title: str
    content: str

    class Config:
        orm_mode = True