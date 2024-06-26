import glob
import os
import aiomysql
from dotenv import load_dotenv

load_dotenv()


async def getMySqlPool():
    return await aiomysql.create_pool(
        host=os.getenv('MYSQL_HOST'),
        port=int(os.getenv('MYSQL_PORT')),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        db=os.getenv('MYSQL_DATABASE'),
        autocommit=True
    )

async def createTableIfNeccessary(dbPool):
    workDirectory = os.getcwd()
    print(f"현재 작업 디렉토리: {workDirectory}")
    sqlFileList = glob.glob('../sql/*sql')
    print(f"sqlFileList: {sqlFileList}")
    async with dbPool.acquire() as connection:
        async with connection.cursor() as cursor:
            for filePath in sqlFileList:
                with open(filePath, 'r') as file:
                    sql = file.read()
                    await cursor.execute(sql)

            # 실제 메모리에 배치되어 있는 정보들을 Disk I/O로 내림
            # commit을 안하면 db에 생성 안될 확률이 높음
            # commit을 안하면 db에 올라갈 가능성은 있지만 보상을 안해줌
            # 내리는 애들이 많아지면 한번에 내리게 된다.
            # 즉 I/O로 내리지 않는다. 그래서 commit을 해줘야 한다.
            await connection.commit()

            # 비동기 프레임워크를 쓸 때는 테이블을 직접 만들어줘야함
            # 자기가 만들어 놓은 테이블 집어 넣고 테이블 집어 넣을때 자동으로 생성되도록