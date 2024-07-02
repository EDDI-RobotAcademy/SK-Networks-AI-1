from abc import abstractmethod, ABC


class OrdersItemRepository(ABC):
    @abstractmethod
    def create(self, orders, product, price, quantity):
        pass
