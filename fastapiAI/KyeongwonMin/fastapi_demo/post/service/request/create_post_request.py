from pydantic import BaseModel

from post.entity.models import Post


class CreatePostRequest(BaseModel):
    title: str
    content: str

    def toPost(self) -> Post:
        return Post(title=self.title, content=self.content)
