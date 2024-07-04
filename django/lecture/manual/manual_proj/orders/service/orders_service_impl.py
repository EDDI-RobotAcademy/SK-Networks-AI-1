from cart.repository.cart_item_repository_impl import CartItemRepositoryImpl
from orders.entity.orders_status import OrderStatus
from orders.repository.orders_item_repository_impl import OrdersItemRepositoryImpl
from orders.repository.orders_repository_impl import OrdersRepositoryImpl
from orders.service.orders_service import OrdersService
from product.repository.product_repository_impl import ProductRepositoryImpl


class OrdersServiceImpl(OrdersService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__ordersRepository = OrdersRepositoryImpl.getInstance()
            cls.__instance.__ordersItemRepository = OrdersItemRepositoryImpl.getInstance()
            cls.__instance.__cartItemRepository = CartItemRepositoryImpl.getInstance()
            cls.__instance.__productRepository = ProductRepositoryImpl.getInstance()

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

    def readOrderDetails(self, orderId, accountId):
        try:
            order = self.__ordersRepository.findById(orderId)
            # print(f"order.account.id: {order.account.id}, accountId: {accountId}")
            # print(f"type(order.account.id): {type(order.account.id)}, type(accountId): {type(accountId)}")
            if order.account.id != int(accountId):
                raise ValueError('Invalid accountId for this order')

            print("check order object <- readOrderDetails()")

            # OrdersItemRepositoryImpl을 통해 해당 주문의 상세 항목들을 조회합니다.
            ordersItemList = self.__ordersItemRepository.findAllByOrder(order)

            totalPrice = sum(ordersItem.total_price() for ordersItem in ordersItemList)

            # 조회된 주문 상세 내역을 필요한 형식으로 반환할 수 있도록 구성합니다.
            order_details = {
                'order': {
                    'id': order.id,
                    'status': order.status,
                    'created_date': order.created_date,
                    'total_price': totalPrice,
                    # 'shipping_address': order.shipping_address,
                    # 'billing_address': order.billing_address,
                },
                'order_items': [
                    {
                        'product_id': item.product_id,
                        'product_name': self.__productRepository.findByProductId(item.product_id).productName,
                        'quantity': item.quantity,
                        'price': item.price,
                        'total_price': item.total_price(),
                    }
                    for item in ordersItemList
                ]
            }

            return order_details

        except Exception as e:
            print('Error reading order details:', e)
            raise e


