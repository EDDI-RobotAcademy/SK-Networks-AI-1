from pydantic import BaseModel


class Post(BaseModel):
    id: int = None
    title: str
    content: str

    class Config:
        # deprecated!!!
        # orm_mode = True
        from_attributes = True
