from django.db import models

class OrdersStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    CONFIRMED = 'COMFIRMED', 'Confired'
    SHIPPED = 'SHIPPED', 'Shipped'
    DELIVERED = 'DELIVERED', 'Delivered'
    CANCELLED = 'CANCELLED', 'Cancelled'