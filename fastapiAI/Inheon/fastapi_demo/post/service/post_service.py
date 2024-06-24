from abc import ABC, abstractmethod
from typing import List

from post.controller.request_form.create_post_request import CreatePostRequest
from post.controller.response_form.create_post_response_form import CreatePostResponseForm
from post.entity.models import Post


class PostService(ABC):
    @abstractmethod
    def postList(self) -> List[Post]:
        pass

    @abstractmethod
    def CreatePostRequest(self, createPostRequest: CreatePostRequest) -> CreatePostResponseForm:
        pass