from abc import ABC, abstractmethod


class CartRepository(ABC):
    @abstractmethod
    def findByAccount(self, account):
        pass
    @abstractmethod
    def register(self, account):
        pass
