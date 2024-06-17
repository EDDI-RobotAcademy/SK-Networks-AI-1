from django.db import models

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=128, null=False)
    productDescription = models.TextField()
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productImage = models.

    # 추후 이미지 관련 필드 추가
    registeredDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName

    class Meta:
        db_table = 'product'