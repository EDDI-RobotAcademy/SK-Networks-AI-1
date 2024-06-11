from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from product.entity.models import Product
from product.serializers import ProductSerializer
from product.service.product_service_impl import ProductServiceImpl


# Create your views here.
# viewsets를 사용하려면 rest_framework가 설정되어야 합니다.
# pip install djangorestframework
class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all()
    productService = ProductServiceImpl.getInstance()

    def list(self, request):
        productList = self.productService.list()
        serializer = ProductSerializer(productList, many=True)
        return Response(serializer.data)
