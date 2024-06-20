from abc import ABC, abstractmethod
class RedisService(ABC):
    @abstractmethod
    def store_access_token(self, account_id, Usertoken):
        pass

    @abstractmethod
    def getValueByKey(self, key):
        pass