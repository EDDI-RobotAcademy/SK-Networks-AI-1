from pydantic import BaseModel

from post.entity.models import Post


class CreatePostResponse(BaseModel):
    id: int
    # @classmethod
    # def toCreatePostResponseForm(cls) -> 'CreatePostResponseForm':
    #     return cls(id=id)

    @classmethod
    def fromPost(cls, entity: Post) -> 'CreatePostResponse':
        return cls(id=entiy.id)