from django.db import models


# Create your models here.
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=30, null=False)
    writer = models.CharField(max_length=32, null=False)
    productDescription = models.TextField()
    productPrice = models.IntegerField(null=False)
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName

    class Meta:
        db_table = "product"
