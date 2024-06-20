from abc import ABC, abstractmethod


class RedisService(ABC):
    @abstractmethod
    def store_access_token(self, account_id, access_token):
        pass