from pydantic import BaseModel

from post.service.request.create_post_request import CreatePostRequest


class CreatePostRequestForm(BaseModel):
    title: str
    content: str

    def toCreatePostRequest(self) -> CreatePostRequest:
        return CreatePostRequest(title=self.title, content=self.content)

# request_form을 사용하는 이유

# form은 항상 웹에서 온다.
# UI 관점에서 보는 domain은 특정 관점에 국한되지 않음
# 상품정보, 회원정보 등이 묶여서 올수도 있음
# 멀티 도메인이 들어오는 경우에는 Request들이 서로 다른 도메인을 타고 들어갈 수 있음
# 여기서 말하는 Request들은 vue에서 오는 Request들
# Request는 서비스에서 쓰기 때문

# 요청방식이 다를 수 있기 때문에
# 생성에 사용하는, 검색에 사용하는, 다른 방식으로 사용하는 request들을 구분하기 위해
# 현재 form앞에 create를 썼다.
# request form은 여러가지가 만들어질 수 있다는 뜻