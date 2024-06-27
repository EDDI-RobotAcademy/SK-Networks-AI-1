from abc import ABC, abstractmethod
from typing import List, Optional


from post.controller.response_form.create_post_response_form import CreatePostResponseForm
from post.entity.models import Post
from post.service.request.create_post_request import CreatePostRequest


class PostService(ABC):

    @abstractmethod
    def postList(self) -> List[Post]:
        pass

    @abstractmethod
    def createPost(self, createPostRequest: CreatePostRequest) -> CreatePostResponseForm:
        pass

    @abstractmethod
    def readPost(self, postId: int) -> Optional[Post]:
        pass