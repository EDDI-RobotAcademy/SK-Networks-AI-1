from rest_framework import serializers

from cart.entity.cart import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['cartId', 'account', 'createdDate', 'updatedDate']
        read_only_fields = ['createdDate', 'updatedDate']