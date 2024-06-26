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
            cls.__instance.__cartRepository = CartRepositoryImpl.getInstance()
            cls.__instance.__productRepository = ProductRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
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
        if cart is None: # 장바구니가 없다면
            print("장바구니 새롭게 생성")
            cart = self.__cartRepository.register(account)

        print("기존 장바구니 사용")

        productId = cartData.get('productId')
        # 기존 아이템 2번이상 넣었나? 체크를 위해 cartItem 객체 호출
        cartItem = self.__cartItemRepository.findByProductId(productId)
        if cartItem is None:
            print("신규 상품 추가")
            product = self.__productRepository.findByProductId(productId)
            self.__cartItemRepository.register(cartData, cart, product)
        else:
            print("기존 상품 추가")

            cartItem.quantity += 1
            self.__cartItemRepository.update(cartItem) # save보단 update가 나음 (register와 save의 모호성이 생김)

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
                'productId': cartItem.product.productId,
                'quantity': cartItem.quantity,
            }
            cartItemListResponseForm.append(cartItemResponseForm)

        return cartItemListResponseForm