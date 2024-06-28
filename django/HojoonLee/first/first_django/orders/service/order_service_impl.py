from cart.repository.cart_item_repository_impl import CartItemRepositoryImpl
from orders.service.order_service import OrderService
from orders.entity.orders_status import OrdersStatus
from orders.repository.orders_repository_impl import OrdersRepositoryImpl
from orders.repository.orders_item_repository_impl import OrdersItemRepositoryImpl

class OrderServiceImpl(OrderService):
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
            # orders객체 생성
            orders = self.__ordersRepository.create(accountId, OrdersStatus.PENDING) # 확인이 안된 정보 Pending

            for item in orderItemList:
                # id를 통해 cartItem 찾기
                cartItem = self.__cartItemRepository.findById(item['cartItemId'])
                # 주문 정보가 담긴 ordersItem 객체 생성
                self.__ordersItemRepository.create(
                    orders,
                    cartItem.product, # 해당 id의 장바구니에 등록된 상품들
                    item['orderPrice'],
                    item['quantity']
                )
            return orders.id

        except Exception as e:
            print('Error Creating order:', e)
            raise e