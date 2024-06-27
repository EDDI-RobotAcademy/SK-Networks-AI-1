import redis
from django.conf import settings

from oauth.service.redis_service import RedisService


class RedisServiceImpl(RedisService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.redis_client = redis.StrictRedis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                password=settings.REDIS_PASSWORD,
                decode_responses=True
            )

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def store_access_token(self, account_id, userToken):
        try:
            self.redis_client.set(userToken, account_id)
        except Exception as e:
            print('Error storing access token in Redis:', e)
            raise e

    def getValueByKey(self, key):
        try:
            return self.redis_client.get(key)
        except Exception as e:
            print("redis key로 value 찾는 중 에러 발생:", e)
            raise e

    def deleteKey(self, key):
        try:
            result = self.redis_client.delete(key)
            if result == 1:
                print(f"유저 토큰 삭제 성공: {key}")
                return True

            return False

        except Exception as e:
            print("redis key 삭제 중 에러 발생:", e)
            raise e