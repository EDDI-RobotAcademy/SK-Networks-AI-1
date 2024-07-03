from rest_framework import serializers
from cart.entity.cart import Cart


class CartSerializer(serializers.ModelSerializer):
    # cartId= serializers.CharField(source='cartId.cartId', read_only=True)
    account = serializers.CharField(source='account.account', read_only=True)

    class Meta:
        model = Cart
        fields = ['account']
