from django.db import models

# Create your models here.
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=128, null=False)
    price = models.CharField(max_length=128, null=False)

    class Meta:
        db_table = 'product'