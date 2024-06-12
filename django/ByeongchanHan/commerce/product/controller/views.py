from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from product.domain.models import Product
from product.serializers import ProductSerializer
from product.service.product_service_impl import ProductServiceImpl


class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all()
    product_service = ProductServiceImpl()

    def list(self, request):
        product_list = self.product_service.list()
        serializer = ProductSerializer(product_list, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            product = self.product_service.create_product(serializer.validated_data)
            return Response(
                ProductSerializer(product).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        product = self.product_service.read_product(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
