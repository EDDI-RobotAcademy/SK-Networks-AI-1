from abc import ABC, abstractmethod


class RedisService(ABC):
    @abstractmethod
    def store_access_token(self, account_id, access_token):
        pass

    @abstractmethod
    def getValueByKey(self, key):
        pass

    @abstractmethod
    def deleteKey(self, key):
        pass