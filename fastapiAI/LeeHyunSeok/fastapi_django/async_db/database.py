import glob
import os
import aiomysql
from dotenv import load_dotenv

load_dotenv()

async def getMySqlPool():
    return await aiomysql.create_pool(
        host=os.getenv('MYSQL_HOST'),
        port=int(os.getenv('MYSQL_PORT')),
        user = os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        db=os.getenv('MYSQL_DATABASE'),
        autocommit=True
    )


async def createTableIfNeccessary(dbPool):
    workDirectory = os.getcwd()
    print(f"현재 디렉토리: {workDirectory}")

    sqlFileList = glob.glob('../sql/*.sql')  #sql dir(디렉토리)의 모든 .sql 파일들을 읽겠다는 의미

    #DB Pool을 획득하여 DB Connection 확보
    async with dbPool.acquire() as connection:    #acquire은 dbPool의 기본 세팅을 가져오겠다?
        #DB Connection에서 정보에 접근할 수 있는 cursor 객체 확보
        async with connection.cursor() as cursor:
            #sql 파일 중 하나
            for filePath in sqlFileList:
                with open(filePath, 'r') as file:   #읽기 전용으로 파일 읽기
                    sql = file.read()
                    await cursor.execute(sql)

            #실제 Memory에 배치되어 있는 정보들을 Disk I/O로 내림 ->실제 db는 Disk에 올리기 때문
            await connection.commit()
