from abc import ABC,abstractmethod
from typing import List, Optional
from post.entity.models import Post


class PostRepository(ABC):
    @abstractmethod
    def list(self) -> List[Post]:
        pass

    @abstractmethod
    def create(self, post: Post) -> int: # post객체를 넣으면 int (id)를 반환
        pass

    @abstractmethod
    def findById(self, postId: int) -> Optional[Post]:
        pass