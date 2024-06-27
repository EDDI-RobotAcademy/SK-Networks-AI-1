from cart.repository.cart_item_repository import CartItemRepository
from cart.entity.cart_item import CartItem

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

    def register(self, cartData, cart, product):
        cartItem = CartItem(
            cart=cart,
            product=product,
            price=cartData.get('productPrice'),
            quantity=cartData.get('quantity'),
        )
        cartItem.save()
        return cartItem

    def update(self, cartItem):
        cartItem.save()

    def findByProductId(self, productId):
        try:
            return CartItem.objects.get(product_id=productId)
        except CartItem.DoesNotExist:
            return None

    def findAllByProductId(self, productId):
        return CartItem.objects.filter(product_id=productId)