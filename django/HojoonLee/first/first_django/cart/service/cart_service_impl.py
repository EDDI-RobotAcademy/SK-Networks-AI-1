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
        if cart is None:
            print("장바구니 새롭게 생성")
            cart = self.__cartRepository.register(account)

        print("기존 장바구니 사용")

        productId = cartData.get('productId')
        print(f"productId: {productId}")

        cartItemList = self.__cartItemRepository.findAllByProductId(productId)
        print(f"cartItemList: {cartItemList}")

        cartItem = None
        for item in cartItemList:
            cartFromCartItem = item.cart
            accountFromCart = cartFromCartItem.account
            if accountFromCart.id == account.id:
                cartItem = item
                break

        if cartItem is None:
            print("신규 상품 추가")
            # 여기서 product 객체를 받았기 때문에, cartItem.product가 가능해짐
            product = self.__productRepository.findByProductId(productId)
            self.__cartItemRepository.register(cartData, cart, product)
        else:
            print("기존 상품 추가")

            cartItem.quantity += 1
            self.__cartItemRepository.update(cartItem)

    def cartList(self, accountId):
        # redis key를 가지고 해당 account 객체 찾기
        account = self.__accountRepository.findById(accountId)
        # 해당 계정의 cart 가져오기 >> 장바구니 목록 가져올 때 사용예정
        cart = self.__cartRepository.findByAccount(account)
        print(f"cartList -> cart: {cart}")
        # 해당 계정의 장바구니 목록 가져오기
        cartItemList = self.__cartItemRepository.findByCart(cart)
        print(f"cartList -> cartItemList: {cartItemList}")

        # controller에 responseForm이 없어서 responseForm 만드는 작업을 여기서 직접 구현한 것임
        # 실제로 여기서는 다양한 도메인이(product, cartItem) 엮여서 포장하는 과정을 진행중
        # 다른 사람들은 여기 부분은 그리 궁금하지 않고 그저 어떻게 돌아가는지만 관심있는데 여기 때문에 코드가 지저분해짐
        cartItemListResponseForm = []

        # cartItem.product 가 가능한 이유는 cartItem entity에서 product를 외래키로 삼았기 때문
        # 이미 register에서 cartItem에 product를 append했기 때문에 이용가능한거 같기도 ?
        for cartItem in cartItemList:
            cartItemResponseForm = {
                'cartItemId': cartItem.cartItemId,
                'productName': cartItem.product.productName,
                'productPrice': cartItem.product.productPrice,
                'productId': cartItem.product.productId,
                'quantity': cartItem.quantity,
                # 'image': cartItem.product.productImage 이렇게 하면 이미지도 처리 가능
            }
            cartItemListResponseForm.append(cartItemResponseForm)

        return cartItemListResponseForm

    # def cartList(self, accountId):
    #     return self.cartRepository.findByAccount(accountId)

    # def cartList(self, accountId):
    #     account = self.__accountRepository.findById(accountId)
    #     print(f"cartList -> account:", account)
    #     if account:
    #         cart = self.__cartRepository.findByAccount(account)
    #         print(f"cartList -> cart:", cart)
    #         if cart:
    #             return cart.items.all()
    #     return []