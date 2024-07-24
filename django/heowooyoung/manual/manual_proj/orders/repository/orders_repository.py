from abc import ABC, abstractmethod


class OrdersRepository(ABC):
    @abstractmethod
    def create(self, accountId, status):
        pass

    @abstractmethod
    def findById(self, orderId):
        pass