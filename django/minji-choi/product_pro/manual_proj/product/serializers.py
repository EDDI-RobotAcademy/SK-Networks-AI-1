from rest_framework import serializers

from product.entity.product import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['productId', 'productName', 'productPrice', 'productCategory', 'productImage', 'writer', 'content', 'regDate', 'updDate']
        read_only_fields = ['regDate', 'updDate']
        