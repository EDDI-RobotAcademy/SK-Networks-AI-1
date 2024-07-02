import os
import aiomysql
from dotenv import load_dotenv
import glob

load_dotenv() # 아래 env 관련쓰니까 dotenv() 실행
async def getMySqlPool():
    return await aiomysql.create_pool(
        host=os.getenv('MYSQL_HOST'),
        port=int(os.getenv('MYSQL_PORT')),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        db=os.getenv('MYSQL_DATABASE'),
        autocommit=True
    )

# 비동기 db는 테이블이 자동으로 생성이 안된다.
# 근데 수동으로 생성하려고 하면 타이핑등 휴먼 에러가 발생할 수 있으므로
# 이렇게 각 domain sql파일을 읽고 에러없이 적절하게 테이블생성하도록 함
async def createTableIfNeccessary(dbPool):
    # app이 cwd라서 디렉토리 한칸위로 올려줘야 함
    sqlFileList = glob.glob('../sql/*.sql') # sql dir의 모든 .sql 파일들 읽기
    # print(f"sqlFileList: {sqlFileList}")
    # DB Pool을 획득하여 DB Connection 확보
    async with dbPool.acquire() as connection:
        # DB Connection에서 정보에 접근할 수 있는 cursor 객체 확보
        async with connection.cursor() as cursor:
            # sql 파일 중 하나
            for filePath in sqlFileList:
                with open(filePath, 'r') as file: # 읽기전용으로 파일 읽기
                    sql = file.read()
                    await cursor.execute(sql)
            # 실제 Memory에 배치되어 있는 정보들을 Disk I/O로 내림 -> 실제 DB는 Disk에 맺히기 때문
            await connection.commit() # 테이블을 db에 커밋 (db 생성을 보장한다.), 여러 db를 처리할 때 유용