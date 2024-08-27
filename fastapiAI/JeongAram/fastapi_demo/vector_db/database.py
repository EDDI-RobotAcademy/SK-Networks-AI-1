import os
import urllib.parse

import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

async def getMongoDBPool():
    host=os.getenv('MONGO_HOST')
    port=int(os.getenv('MONGO_PORT'))
    user=os.getenv('MONGO_USER')
    password=os.getenv('MONGO_PASSWORD')
    db=os.getenv('MONGO_DATABASE')

    if isinstance(password, bytes):
        password = password.decode('utf-8')
    elif password is not None:
        password = str(password)

    password = urllib.parse.quote_plus(password)

    uri = f"mongodb://{user}:{password}@{host}:{port}/{db}"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    mongoDB = client[db]

    return mongoDB