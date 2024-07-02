from pydantic import BaseModel

from post.service.request.create_post_request import CreatePostRequest

class CreatePostRequestForm(BaseModel):
    title: str
    content: str

    # 앞에 create를 붙이는 이유는 요청 방식이 다를 수 있기 때문에 구별하기 위해서 사용
    def toCreatePostRequest(self) -> CreatePostRequest:
        return CreatePostRequest(title=self.title, content=self.content)

    # request form 쓰는 이유?
    # 멀티 도메인이 들어올 때 분리해서 처리하기 위해 사용
    # 분리 후 각 도메인의 서비스로 보내진다.
    # 순서: web에서의 request -> fastapi에서의 requestform -> request -> service -> repository
    # -> response -> responseform -> web