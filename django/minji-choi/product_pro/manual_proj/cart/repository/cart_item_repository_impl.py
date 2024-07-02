from cart.repository.cart_item_repository import CartItemRepository
from cart.entity.cart_item import CartItem
from product.entity.product import Product


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
            productPrice=productPrice
        )

    def findByProductId(self, productId):
        try:
            return CartItem.objects.get(product_id=productId)
        except CartItem.DoesNotExist:
            return None

    def findAllByProduct(self, product):
        return CartItem.objects.filter(product=product)
    def findByCart(self, cart):
        return list(CartItem.objects.filter(cart=cart))

    def update(self, cartItem):
        cartItem.save()
    def findById(self, id):
        return CartItem.objects.get(cartItemId=id)

