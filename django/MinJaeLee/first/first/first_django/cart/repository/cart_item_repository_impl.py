from cart.entity.cart import Cart
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
        productPrice = cartData.get('productPrice')
        quantity = cartData.get('quantity')

        CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=quantity,
            price=productPrice
        )

    def findByCart(self, cart):
        return list(CartItem.objects.filter(cart=cart))

    def findByProductId(self, productId):
        try:
            return CartItem.objects.get(product_id=productId)
        except CartItem.DoesNotExist:
            return None

    def update(self, cartItem):
        cartItem.save()

    def findAllByProductId(self, productId):
        # 단수 출력의 경우 None 출력으로 오류가 날 수 있으나
        # 아래 filter를 사용하면 내용이 없어도 빈 리스트가 반환되기에
        # try except 구문이 필요 없음.
        return CartItem.objects.filter(product_id = productId)
