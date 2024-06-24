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
    sqlFileList = glob.glob('../sql/*.sql')

    # DB Pool을 획득하여 DB Connection 확보
    async with dbPool.acquire() as connection:
        # DB Connection에서 정보에 접근할 수 있는 cursor 객체 확보
        async with connection.cursor() as cursor:
            # sql 파일 중 하나
            for filePath in sqlFileList:
                with open(filePath, 'r') as file:
                    sql = file.read()
                    await cursor.execute(sql)
            # 실재 Memory에 배치되어 있는 정보들을 Disk I/O로 내림
            await connection.commit()