from pydantic import BaseModel

from post.service.request.create_post_request import CreatePostRequest

class CreatePostRequestForm(BaseModel):
    title: str
    content: str

    # 앞에 create를 붙이는 이유는 요청 방식이 다를 수 있기 때문에 구별하기 위해서 사용
    def toCreatePostRequest(self) -> CreatePostRequest:
        return CreatePostRequest(title=self.title, content=self.content)