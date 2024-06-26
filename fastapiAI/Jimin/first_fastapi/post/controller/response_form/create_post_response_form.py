from pydantic import BaseModel

from post.service.response.create_post_response import CreatePostResponse


class CreatePostResponseForm(BaseModel):
    id: int

    @classmethod
    def fromCreatePostResponse(cls, response: CreatePostResponse) -> 'CreatePostResponseForm':
        return cls(id=response.id)
    # response 할 때 id 값만 오면 됨
    # @classmethod의 cls = 그 클래스의 생성자, 클래스 자기 자신