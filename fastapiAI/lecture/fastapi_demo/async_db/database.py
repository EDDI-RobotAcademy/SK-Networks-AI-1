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

    sqlFileList = glob.glob('../sql/*.sql')
    print(f"sqlFileList: {sqlFileList}")

    async with dbPool.acquire() as connection:
        async with connection.cursor() as cursor:
            for filePath in sqlFileList:
                with open(filePath, 'r') as file:
                    sql = file.read()
                    await cursor.execute(sql)

            await connection.commit()
