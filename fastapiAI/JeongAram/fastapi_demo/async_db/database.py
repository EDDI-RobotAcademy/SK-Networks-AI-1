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

    sqlFileList = glob.glob('../sql/*.sql') # glob: sql dir의 모든 .sql 파일들 다 읽겠다
    print(f"sqlFileList: {sqlFileList}")

    # DB Pool을 획득하여 DB connection 확보
    async with dbPool.acquire() as connection:
        # DB connection에서 정보에 접근할 수 있는 cursor 객체 확보
        async with connection.cursor() as cursor:
            # sql 파일 중 하나
            for filePath in sqlFileList:
                with open(filePath, 'r') as file:
                    sql = file.read()
                    await cursor.execute(sql)

            # 실제 Memory에 배치되어 있는 정보들을 Dist I/O로 내림
            # connection.commit()을 하지 않아도 테이블이 만들어질 수 있지만 보장되지는 않음
            # 내리는 데이터의 양이 많아지면 한번에 내린다.
            # 많은 요청이 들어왔을 때 일부 데이터가 누락될 수 있기 때문에
            # 즉, 양이 많아지게 되면 I/O로 내리지 않고 모아두고 있음
            await connection.commit()

            # 비동기 프레임워크에서는 db테이블을 자동으로 만들어주지 못하기 때문에
            # 실제로 테이블을 만들어줘야 한다.
            # 만들어 놓은 테이블에 집어 넣을 때 자동으로 생성되도록?