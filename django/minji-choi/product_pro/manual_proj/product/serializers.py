from rest_framework import serializers

from product.entity.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productId', 'prodname', 'price', 'productImage', 'writer', 'content', 'regDate', 'updDate']
        read_only_fields = ['regDate', 'updDate']
        