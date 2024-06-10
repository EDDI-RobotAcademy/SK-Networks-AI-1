from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from product.entity.models import Product
from product.service.product_service_impl import ProductServiceImpl
from product.serializers import ProductSerializer


# Create your views here.
class ProductView(viewsets.Viewset):
    queryset = Product.objects.all()
    productService = ProductServiceImpl.getInstance()

    def create(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            product = self.productService.createProduct(serializer.validated_data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    