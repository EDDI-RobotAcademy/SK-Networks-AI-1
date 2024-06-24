from pydantic import BaseModel

from post.service.response.create_post_response import CreatePostResponse


class CreatePostResponseForm(BaseModel):
    id: int
    @classmethod
    def fromCreatePostResponse(cls, response: CreatePostResponse) -> 'CreatePostResponseForm':
        return cls(id = response.id)
