from typing import List

from aiomysql import Pool

from post.entity.models import Post
from post.repository.post_repository import PostRepository


class PostRepositoryImpl(PostRepository):
    def __init__(self, db_pool: Pool):
        self.dbPool = db_pool

    def list(self) -> List[Post]:
        print("list()")


