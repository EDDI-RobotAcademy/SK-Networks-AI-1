from django.db import models

from cart.entity.cart import Cart
from product.entity.models import Product


# Create your models here.
class CartItem(models.Model):
    cartItemId = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (f"CartItem -> id: {self.cartItemId},"
                f"cart -> id: {self.cart.cartId},"
                f"product -> id: {self.product.productName},"
                f"quantity -> id: {self.quantity},")

    class Meta:
        db_table = 'cart_item'
        app_label = 'cart'