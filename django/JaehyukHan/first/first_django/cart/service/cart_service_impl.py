from account.repository.account_repository_impl import AccountRepositoryImpl
from product.repository.product_repository_impl import ProductRepositoryImpl
from cart.repository.cart_repository_impl import CartRepositoryImpl
from cart.repository.cart_item_repository_impl import CartItemRepositoryImpl
from cart.service.cart_service import CartService


class CartServiceImpl(CartService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__cartRepository = CartRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
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

        print(f"account: {account}, cart: {cart}")
        if cart is None:
            cart = self.__cartRepository.register(account)

        productId = cartData.get('productId')
        print(f"productId: {productId}")
        cartItemList = self.__cartItemRepository.findAllByProductId(productId)
        print(f"cartItems: {cartItemList}")

        cartItem = None
        for item in cartItemList:
            cartFromCartItem = item.cart
            accountFromCart = cartFromCartItem.account
            if accountFromCart.id == account.id:
                cartItem = item
                break

        if cartItem is None:
            product = self.__productRepository.findByProductId(cartData.get('productId'))
            self.__cartItemRepository.register(cartData, cart, product)
        else:
            cartItem.quantity += 1
            self.__cartItemRepository.update(cartItem)

    def cartList(self, accountId):
        # 내가 작성한 코드
        # account = self.__accountRepository.findById(accountId)
        # cart = self.__cartRepository.findByAccount(account)
        # cartItems = self.__cartItemRepository.findByCart(cart)
        # cartList = []
        #
        # for cartItem in cartItems:
        #     if cartItem.cart == cart:
        #         cartInfo = [cartItem.product.productName, cartItem.price, cartItem.quantity, cartItem.price * cartItem.quantity]
        #         cartList.append(cartInfo)
        #
        # return cartList
        account = self.__accountRepository.findById(accountId)
        cart = self.__cartRepository.findByAccount(account)
        print(f"cartList -> cart: {cart}")
        cartItemList = self.__cartItemRepository.findByCart(cart)
        print(f"cartList -> cartItemList: {cartItemList}")
        cartItemListResponseForm = []

        for cartItem in cartItemList:
            cartItemResponseForm = {
                'cartItemId': cartItem.cartItemId,
                'productName': cartItem.product.productName,
                'productPrice': cartItem.product.productPrice,
                'productId': cartItem.product.productId,
                'quantity': cartItem.quantity,
            }
            cartItemListResponseForm.append(cartItemResponseForm)

        return cartItemListResponseForm
