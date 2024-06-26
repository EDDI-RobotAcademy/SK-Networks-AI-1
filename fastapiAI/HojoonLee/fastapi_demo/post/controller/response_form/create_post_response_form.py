from pydantic import BaseModel

from post.service.response.create_service_response import CreatePostResponse


class CreatePostResponseForm(BaseModel):
    id: int

    # service에서 만들어진 response를(=CreatePostResponse) 통해서 form을 만든다.
    # service의 response가 -> responseForm이 된다 라는 뜻  == (cls, response: CreatePostResponse) -> 'CreatePostResponseForm':
    # response는 여기를 거쳐서 responseform으로 바뀐다.
    @classmethod
    def fromCreatePostResponse(cls, response: CreatePostResponse) -> 'CreatePostResponseForm':
        # CreatePostResponse는 service/response 에서 구현
        return cls(id=response.id) # 작성한 게시물의 번호만 return