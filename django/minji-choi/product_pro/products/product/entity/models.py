from django.db import models

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    prodname = models.CharField(max_length=128, null=False)
    price = models.IntegerField(null=False)
    writer = models.CharField(max_length=32, null=False)
    content = models.TextField()
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prodname

    class Meta:
        db_table = 'product'
