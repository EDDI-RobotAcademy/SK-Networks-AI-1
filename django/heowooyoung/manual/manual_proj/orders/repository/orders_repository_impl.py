from orders.entity.orders import Orders
from orders.repository.orders_repository import OrdersRepository


class OrdersRepositoryImpl(OrdersRepository):
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

    def create(self, accountId, status):
        orders = Orders(account_id=accountId, status=status)
        orders.save()

        return orders

    def findById(self, orderId):
        return Orders.objects.get(id=orderId)