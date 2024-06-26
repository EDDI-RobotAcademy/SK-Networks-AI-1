from django.db import models


# Create your models here.
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=128, null=False)
    productDescription = models.TextField()
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productImage = models.CharField(max_length=100, null=True)

    # 추후 이미지 관련 업로드
    registeredDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName

    class Meta:
        db_table = "product"