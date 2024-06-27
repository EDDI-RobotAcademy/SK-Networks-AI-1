from pydantic import BaseModel

from post.service.request.create_post_request import CreatePostRequest


class CreatePostRequestForm(BaseModel):
    title: str
    content: str

    def toCreatePostRequest(self) -> CreatePostRequest:
        return CreatePostRequest(title=self.title, content=self.content)