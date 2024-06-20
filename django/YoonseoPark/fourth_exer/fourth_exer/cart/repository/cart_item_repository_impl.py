from cart.entity.cart_item import CartItem
from cart.repository.cart_item_repository import CartItemRepository


class CartItemRepositoryImpl(CartItemRepository):
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

    def findByProductName(self, productName):
        pass

    def register(self, cartData, cart, product):
        productPrice = cartData.get('productPrice')
        quantity = cartData.get('quantity')

        cartItem = CartItem(
            cart = cart,
            product = product,
            quantity = quantity,
            price = productPrice
        )
        cartItem.save()
        return cartItem


