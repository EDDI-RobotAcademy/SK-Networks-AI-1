from typing import List, Optional

from post.entity.models import Post
from post.repository.post_repository import PostRepository
from aiomysql import Pool # aiomysql을 통해서 비동기 db에 관한 sql을 지원 <-> sqlalchemy는 자동화라 비동기와는 어울리지 않음

class PostRepositoryImpl(PostRepository):
    def __init__(self, db_pool: Pool): # db_pool이 입력인자로 오는데 default format이 Pool 이라는 뜻
        self.dbPool = db_pool

    async def list(self) -> List[Post]:
        print("list()")

        # aiomysql를 쓰면 비동기 처리가 가능 하지만, 비동기 처리를 위해 db를 수동으로 다뤄줘야 함
        async with self.dbPool.acquire() as connection:
            async with connection.cursor() as cur: # 같은 커서를 가지고 있다면(=여러 스레드가 같은 일을 요청) 비동기로 처리
                await cur.execute("select id, title, content from post") # 쿼리문 실행 by aiomysql
                result = await cur.fetchall() # 모든 정보 다 받을거니까 fetchall
                postList = [Post(id=row[0], title=row[1], content=row[2]) for row in result]
                return postList

    async def create(self, post: Post) -> int:
        print("post create()")

        async with self.dbPool.acquire() as connection:
            async with connection.cursor() as cur:
                await cur.execute(
                    "insert into post (title, content) values (%s, %s)",
                    (post.title, post.content)
                )
                await connection.commit() # db io상에 매핑하기위해서 commit
                await cur.execute("select last_insert_id()") # 마지막으로 입력된 id를 알려주세요
                postId = await cur.fetchone() # 1개만 받고싶을 때 fetchone
                return postId[0]

    async def findById(self, postId: int) -> Optional[Post]:
        print("post read()")
        async with self.dbPool.acquire() as connection:
            async with connection.cursor() as cur:
                await cur.execute(
                    "select id, title, content from post where id = %s",
                    (postId,)
                )
                # i/o 처리라 commit할 필요는 없음
                result = await cur.fetchone()  # 1개만 받고싶을 때 fetchone
                if result:
                    return Post(id=result[0], title=result[1], content=result[2])
                return None