from typing import List

from aiomysql import Pool

from post.entity.models import Post
from post.repository.post_repository_impl import PostRepositoryImpl
from post.service.post_service import PostService


class PostServiceImpl(PostService):
    def __init__(self, db_pool: Pool):
        self.__postRepository = PostRepositoryImpl(db_pool)

    async def postList(self) -> List[Post]:
        return await self.__postRepository.list()


