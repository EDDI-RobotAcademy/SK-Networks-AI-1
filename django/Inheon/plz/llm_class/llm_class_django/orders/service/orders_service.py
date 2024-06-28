from abc import ABC, abstractmethod


class OrdersService(ABC):
    @abstractmethod
    def createOrder(self, accountId, orderItemList):
        pass
