from pydantic import BaseModel

class Post(BaseModel):
    id: int = None
    title: str
    content: str

    class Config:
        from_attributes = True
        # orm_mode = True