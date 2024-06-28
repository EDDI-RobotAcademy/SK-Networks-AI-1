from pydantic import BaseModel

from post.service.request.create_post_request import CreatePostRequest


class CreatePostRequestForm(BaseModel):
    title: str
    content: str

 #request form을 쓰는 이유 -> ui에서의 요청은 특정 도메인에 국한되지 않기 때문에. 즉, 멀티 도메인이 들어오는 경우 분리해서 처리하기 위함 여기서 분리해주고 이후에 다른 도메인으로 보내진다.
    def toCreatePostRequest(self) -> CreatePostRequest:
        return CreatePostRequest(title=self.title, content=self.content)
