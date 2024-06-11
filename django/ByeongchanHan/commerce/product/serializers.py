from rest_framework import serializers

from product.domain.models import Product


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "product_id",
            "product_name",
            "seller",
            "price",
            "reg_date",
            "update_date",
        ]
        read_only_fields = ["reg_date", "update_date"]
