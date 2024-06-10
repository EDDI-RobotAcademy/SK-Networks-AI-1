from rest_framework import serializers
from product.entity.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'product_description', 'created_at']
        read_only_fields = ['created_at']
