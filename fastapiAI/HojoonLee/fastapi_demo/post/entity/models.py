from pydantic import BaseModel

class Post(BaseModel):
    id: int = None
    title: str
    content: str

    class Config:
        # 계속 warning 뜨던거 해결
        # orm_mode = True
        from_attributes = True