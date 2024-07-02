from abc import ABC, abstractmethod
class CartRepository(ABC):
    @abstractmethod
    def findByAccount(self, accountId):
        pass
    @abstractmethod
    def register(self, account):
         pass
