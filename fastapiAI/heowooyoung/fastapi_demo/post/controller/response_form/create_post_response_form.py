from pydantic import BaseModel

from post.service.response.create_post_response import CreatePostResponse


class CreatePostResponseForm(BaseModel):
    id: int

    # classmethod에서 cls가 들어있다는 거는 return 한다는 뜻 지금은 자기 자신을 return함
    @classmethod
    def fromCreatePostResponse(cls, response: CreatePostResponse) -> 'CreatePostResponseForm':
        return cls(id=response.id)