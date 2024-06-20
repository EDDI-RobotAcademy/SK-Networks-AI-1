from django.db import models

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=128, null=False)
    productDescription = models.TextField()
    productPrice = models.Decimal