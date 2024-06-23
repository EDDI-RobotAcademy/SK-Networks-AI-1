from abc import ABC, abstractmethod


class RedisService(ABC):
    @abstractmethod
    def store_access_token(self, account_id, userToken):
        pass

    @abstractmethod
    def getValueBykey(self, key):
        pass