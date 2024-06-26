from typing import List, Optional

from aiomysql import Pool

import post
from post.entity.models import Post
from post.repository.post_repository import PostRepository


class PostRepositoryImpl(PostRepository):
    def __init__(self, db_pool: Pool):
        self.dbPool = db_pool

    async def list(self) -> List[Post]:
        print("repository -> list()")

        async with self.dbPool.acquire() as connection:
            #post에 있는 모든 id, title, content를 찾아와서 postList를 만들어 변환
            async with connection.cursor() as cur:
                await cur.execute("select id, title, content from post")
                result = await cur.fetchall()
                postList = [Post(id=row[0], title=row[1], content=row[2]) for row in result]
                return postList

    async def create(self, post: Post) -> int:
        async with self.dbPool.acquire() as connection:
            #post에 있는 모든 id, title, content를 찾아와서 postList를 만들어 변환
            async with connection.cursor() as cur:
                await cur.execute(
                    "insert into post(title, content) values(%s,%s)",
                    (post.title, post.content)
                )
                await connection.commit()
                await cur.execute("select last_insert_id()")
                postId = await cur.fetchone()
                return postId[0]


    async  def findById(self, postId: int) -> Optional[post]:
        async with self.dbPool.acquire() as connection:
            async with connection.cursor() as cur:
                await cur.execute(
                    "select id, title, content from post where id = %s",
                    (postId)
                )
                result = await cur.fetchone()
                if result:
                    return Post(id=result[0], title=result[1], content=result[2])

                return None







