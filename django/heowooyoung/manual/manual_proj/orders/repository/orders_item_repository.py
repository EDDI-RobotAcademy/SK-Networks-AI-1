from abc import ABC, abstractmethod


class OrdersItemRepository(ABC):
    @abstractmethod
    def create(self, orders, product, price, quantity):
        pass

    @abstractmethod
    def findAllByOrder(self, order):
        pass