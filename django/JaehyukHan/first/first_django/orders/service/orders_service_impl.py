from cart.repository.cart_item_repository_impl import CartItemRepositoryImpl
from orders.entity.orders_status import OrderStatus
from orders.repository.orders_item_repository_impl import OrdersItemRepositoryImpl
from orders.repository.orders_repository_impl import OrdersRepositoryImpl
from orders.service.orders_service import OrdersService


class OrdersServiceImpl(OrdersService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__ordersRepository = OrdersRepositoryImpl.getInstance()
            cls.__instance.__ordersItemRepository = OrdersItemRepositoryImpl.getInstance()
            cls.__instance.__cartItemRepository = CartItemRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createOrder(self, accountId, orderItemList):
        try:
            orders = self.__ordersRepository.create(accountId, OrderStatus.PENDING)

            for item in orderItemList:
                cartItem = self.__cartItemRepository.findById(item['cartItemId'])
                self.__ordersItemRepository.create(
                    orders,
                    cartItem.product,
                    item['orderPrice'],
                    item['quantity']
                )

            return orders.id

        except Exception as e:
            print('Error creating order:', e)
            raise e
