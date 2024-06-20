from account.repository.account_repository_impl import AccountRepositoryImpl

from cart.repository.cart_item_repository_impl import CartItemRepositoryImpl
from cart.repository.cart_repository_impl import CartRepositoryImpl
from cart.service.cart_service import CartService
from product.repository.product_repository_impl import ProductRepositoryImpl


class CartServiceImpl(CartService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__cartRepository = CartRepositoryImpl.getInstance()
            cls.__instance.__productRepository = ProductRepositoryImpl.getInstance()
            cls.__instance.__cartItemRepository = CartItemRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def cartRegister(self, cartData, accountId):
        account = self.__accountRepository.findById(accountId) # 사용자 계정을 찾는다.
        cart = self.__cartRepository.findByAccount(account)

        if cart is None: # 사용자 계정과 관련하여 cart가 존재하는지 찾는다
            cart = self.__cartRepository.register(account) # 존재하지 않는다면 새로 cart를 생성한다.

        product = self.__productRepository.findByProductId(cartData.get('productId')) # cartItem에 등록한 product를 찾는다

        self.__cartItemRepository.register(cartData, cart, product) # 필요한 정보를 모두 확보했으므로 cartItem을 생성한다

