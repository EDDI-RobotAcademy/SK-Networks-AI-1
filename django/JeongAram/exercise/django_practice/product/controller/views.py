from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from product.serializers import ProductSerializer
from product.service.product_service_impl import ProductRepositoryImpl
from product.entitiy.models import Product
from product.service.product_service_impl import ProductServiceImpl

# Create your views here.
# viewsets를 사용하려면 rest_framework가 설정되어야 합니다.
# pip install djangorestframework

class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all()
    productService = ProductServiceImpl.getInstance()

    def list(self,request):
        productList = self.productService.list()
        serializer = ProductSerializer(productList, many=True)
        return Response(serializer.data)

    def register(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = self.productService.createProduct(serializer.validated_data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        product = self.productService.readProduct(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def removeProduct(self, request, pk=None):
        self.productService.removeProduct(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def modifyProduct(self, request, pk=None):
        product = self.productService.readProduct(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            updatedProduct = self.productService.updateProduct(pk, serializer.validated_data)
            return Response(ProductSerializer(updatedProduct).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







