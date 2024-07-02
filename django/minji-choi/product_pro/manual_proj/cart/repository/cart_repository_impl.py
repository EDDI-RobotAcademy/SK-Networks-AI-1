from cart.entity.cart import Cart
from cart.repository.cart_repository import CartRepository
class CartRepositoryImpl(CartRepository):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def findByAccount(self, account):
        try:
            cart = Cart.objects.get(account=account)
            return cart
        except Cart.DoesNotExist:
            print('cart is None.')
            return None

    def register(self, account):
        print('카트가 없어서 카트 만들기')
        cart = Cart.objects.create(account=account)
        # return cart 리턴 없어도 됨