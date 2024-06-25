from rest_framework import serializers

from product.entity.models import Product


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productId', 'productName', 'productPrice', 'productDescription', 'productImage', 'registeredDate',
                  'updatedDate']
        read_only_fields = ['registeredDate', 'updatedDate']
