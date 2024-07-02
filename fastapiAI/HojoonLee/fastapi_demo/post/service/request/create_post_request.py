from pydantic import BaseModel # BaseModel의 역할?

from post.entity.models import Post


class CreatePostRequest(BaseModel):
    title: str
    content: str

    def toPost(self) -> Post: # 이 함수를 통해 Post 객체 반환하겠다고 명시
        return Post(title=self.title, content=self.content)

