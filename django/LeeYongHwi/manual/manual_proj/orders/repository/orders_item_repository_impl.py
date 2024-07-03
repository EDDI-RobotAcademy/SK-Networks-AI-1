from orders.repository.orders_item_repository import OrdersItemRepository
from orders.entity.orders_item import OrdersItem

class OrdersItemRepositoryImpl(OrdersItemRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, orders, product, price, quantity):
        orderItem = OrdersItem(orders=orders, product=product, price=price, quantity=quantity)
        orderItem.save()
