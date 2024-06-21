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

    def register(self, cartData, cart, product):
        # 내가 작성한 코드
        # cartItem = CartItem(
        #     cart=cart,
        #     product=product,
        #     price=product.productPrice
        # )
        # cartItem.save()
        # return cartItem
        productPrice = cartData.get('productPrice')
        quantity = cartData.get('quantity')

        CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=quantity,
            price=productPrice
        )

    def findByProduct(self, product):
        try:
            return CartItem.objects.get(product=product)
        except CartItem.DoesNotExist:
            return None

    def update(self, cartItem):
        cartItem.save()
