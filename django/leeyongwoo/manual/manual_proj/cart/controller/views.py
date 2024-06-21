from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from cart.service.cart_service_impl import CartServiceImpl
from product.serializers import ProductSerializer
from product.service.product_service_impl import ProductServiceImpl


class CartView(viewsets.ViewSet):
    cartService = CartServiceImpl.getInstance()

    # def list(self, request):
    #     productList = self.productService.list()
    #     serializer = ProductSerializer(productList, many=True)
    #     return Response(serializer.data)

    def cartRegister(self, request):
        try:
            data = request.data
            print('data:', data)

            self.cartService.cartRegister(data)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('상품 등록 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
