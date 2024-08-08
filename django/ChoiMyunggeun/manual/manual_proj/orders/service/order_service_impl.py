
class OrderServiceImpl(OrderService):
    __instance = None

    def __next__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__ordersRepository = ordersRepositoryImpl.getInstamce()
            cls.__instance.__ordersItemRepository = orderItemRepositoryImpl.getInstamce()
            cls.__instance.__cartItemRepository = cartItemRepositoryImpl.getInstamce()

        return cls.__instance

    @classmethod
    def getInstance(cls):


    def createOrder(self, accountId, orderItemList):
        try:
            orders = self.__ordersRepository.create(accountId, OrderStatus.PENDING)

            for item in orderItemList:
                cartItem = self.__cartItemRepository.findById(item['cartItemId'])
                self.__ordersItemRepositiry.create(
                    orders,
                    cartItem.product,
                    item['orderPrice'],
                    item['quantity']
                )

                return orders.id

        except Exception as e:
            print('Errorrr creationg order:', e)
            return e
