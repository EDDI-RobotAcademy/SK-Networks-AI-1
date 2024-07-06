from cart.repository.cart_repository_impl import CartRepositoryImpl
from cart.repository.cart_item_repository_impl import CartItemRepositoryImpl
from cart.service.cart_service import CartService
from account.repository.account_repository_impl import AccountRepositoryImpl
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
    def cartList(self, accountId):
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
                'productImage': cartItem.product.productImage,
                'productId': cartItem.product.productId,
                'quantity': cartItem.quantity,
            }
            cartItemListResponseForm.append(cartItemResponseForm) # responseFrom을 list로 변환하기 위한 과정

        return cartItemListResponseForm


    def cartRegister(self, cartData, accountId):
        account = self.__accountRepository.findById(accountId) # 있음
        cart = self.__cartRepository.findByAccount(account)

        if cart is None:
            cart = self.__cartRepository.register(account)
        print('이미 있는 cart ')
        productId = cartData.get('productId')
        product = self.__productRepository.findByProductId(productId)
        cartItems = self.__cartItemRepository.findAllByProduct(product)
        cartItem = None
        for item in cartItems:
            cartFromCartItem = item.cart
            accountFromCart = cartFromCartItem.account
            if accountFromCart.id == account.id:
                cartItem = item
                break

        if cartItem is None:
            print('신규 상품 추가')
            product = self.__productRepository.findByProductId(productId) # 있음
            return self.__cartItemRepository.register(cartData, cart, product)
        else:
            print('기존 상품 추가')
            cartItem.quantity += 1
            self.__cartItemRepository.update(cartItem)

    def removeCartItem(self, accountId, cartItemId):
        pass


