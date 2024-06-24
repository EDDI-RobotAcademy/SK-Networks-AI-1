from typing import List

from aiomysql import Pool

from post.entity.models import Post
from post.repository.post_repository import PostRepository


class PostRepositoryImpl(PostRepository):
    def __init__(self, db_pool: Pool):
        self.dbPool = db_pool

    async def list(self) -> List[Post]:
        print("repository -> list()")

        async with self.dbPool.acquire() as connection:
            async with connection.cursor() as cur:
                # post에 있는 모든 id, title, content를 찾아와서 postList를 만들어 반환
                await cur.execute("select id, title, content from post")
                result = await cur.fetchall()
                postList = [Post(id=row[0], title=row[1], content=row[2]) for row in result]
                return postList



