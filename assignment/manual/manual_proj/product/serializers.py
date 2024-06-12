from rest_framework import serializers

from product.entity.models import Product


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productId', 'product_name', 'price', 'product_description', 'regDate', 'updDate']
        read_only_fields = ['regDate', 'updDate']
        