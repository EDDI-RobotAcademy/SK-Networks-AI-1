from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    product_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'product'