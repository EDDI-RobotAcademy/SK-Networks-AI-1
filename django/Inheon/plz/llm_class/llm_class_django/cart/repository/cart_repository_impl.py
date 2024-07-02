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

    def register(self, account):
        return Cart.objects.create(account=account)

    def findByAccount(self, account):
        try:
            return Cart.objects.get(account=account)
        except Cart.DoesNotExist:
            return None

