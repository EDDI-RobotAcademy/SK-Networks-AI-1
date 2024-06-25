from abc import ABC, abstractmethod
from typing import List
from post.entity.models import Post


class PostRepository(ABC):
    @abstractmethod
    def list(self) -> List[Post]:
        pass

    @abstractmethod
    def create(self, post: Post) -> int:
        pass
