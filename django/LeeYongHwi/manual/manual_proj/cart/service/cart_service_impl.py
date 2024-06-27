from cart.service.cart_service import CartService

from account.repository.account_repository_impl import AccountRepositoryImpl
from cart.repository.cart_repository_impl import CartRepositoryImpl
from product.repository.product_repository_impl import ProductRepositoryImpl
from cart.repository.cart_item_repository_impl import CartItemRepositoryImpl


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
        account = self.__accountRepository.findById(accountId)
        cart = self.__cartRepository.findByAccount(account)
        if cart is None:
            print("장바구니 새로 생성")
            cart = self.__cartRepository.register(account)
        print("기존 장바구니 사용")

        productId = cartData.get('productId')
        cartItemList = self.__cartItemRepository.findAllByProductId(productId)

        cartItem = None
        for item in cartItemList:
            cartFromCartItem = item.cart
            accountFromCart = cartFromCartItem.account
            if accountFromCart.id == account.id:
                cartItem = item
                break

        if cartItem is None:
            print("신규 상품 추가")
            product = self.__productRepository.findByProductId(productId)
            self.__cartItemRepository.register(cartData, cart, product)
        else:
            print("기존 상품 추가")
            cartItem.quantity += 1
            self.__cartItemRepository.update(cartItem)
