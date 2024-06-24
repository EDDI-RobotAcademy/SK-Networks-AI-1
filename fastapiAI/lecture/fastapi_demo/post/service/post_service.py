from abc import ABC, abstractmethod
from typing import List

from post.entity.models import Post


class PostService(ABC):
    @abstractmethod
    def postList(self) -> List[Post]:
        pass
