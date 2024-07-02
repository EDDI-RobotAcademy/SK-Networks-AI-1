from abc import ABC, abstractmethod


class OrdersRepository(ABC):
    @abstractmethod
    def create(self, accountId, status):
        pass
