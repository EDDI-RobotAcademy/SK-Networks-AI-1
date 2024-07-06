from django.db import models

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=128, null=False)
    productPrice = models.IntegerField(null=False)
    productCategory = models.CharField(max_length=10, null=False)
    writer = models.CharField(max_length=32, null=False)
    content = models.TextField()
    productImage = models.CharField(max_length=100) # 이미지 경로가 들어간다
    # 추후 이미지 관련 필드 추가
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName

    class Meta:
        db_table = 'product'
