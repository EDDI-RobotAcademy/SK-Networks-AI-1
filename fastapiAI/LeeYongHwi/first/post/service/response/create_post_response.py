from pydantic import BaseModel

from post.entity.models import Post


class CreatePostResponse(BaseModel):
    id: int

    @classmethod
    def fromPost(cls, entity: Post) -> 'CreatePostResponse':
        return cls(id=entity.id)