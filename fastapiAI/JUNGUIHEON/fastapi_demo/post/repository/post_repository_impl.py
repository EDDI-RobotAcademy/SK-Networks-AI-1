from post.repository.post_repository import PostRepository
from aiomysql import Pool
from typing import List

from post.entity.models import Post


class PostRepositoryImpl(PostRepository):
    def __init__(self, db_pool:Pool):
        self.dbPool = db_pool
    def list(self) -> List[Post]:
        print("list()")