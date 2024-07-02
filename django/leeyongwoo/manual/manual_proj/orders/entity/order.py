from django.db import models

from account.entity.account import Account
from django.utils import timezone

from order.entity.order_status import OrderStatus


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    order_date = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_address = models.CharField(max_length=255)
    billing_address = models.CharField(max_length=255)

    def __str__(self):
        return f"Order {self.order_id} by {self.account}"

    class Meta:
        db_table = 'order'
        app_label = 'product_order'
