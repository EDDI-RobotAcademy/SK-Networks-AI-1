from pydantic import BaseModel

from post.service.request.create_post_request import CreatePostRequest


class CreatePostRequestForm(BaseModel):
    title: str
    content: str

    # request form 쓰는 이유? : ui에서의 요청은 특정 도메인에 국한되지 않기 때문
    # 멀티 도메인이 들어오는 경우 분리해서 처리하기 위함 -> 여기서 분리해주고 이후 각 도메인의 서비스로 보내진다.
    # request form -> request로 변환
    def toCreatePostRequest(self) -> CreatePostRequest:
        return CreatePostRequest(title=self.title, content=self.content)