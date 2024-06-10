from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from product.entity.models import Product
from product.serializers import ProductSerializer
from product.service.product_service_impl import ProductServiceImpl


# viewsets를 사용하려면 rest_framework가 설치되어야 합니다.
# pip install dgangorestframework
class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all() # 보드가 어떻게 되어있든 난 다 조회할거야
    productService = ProductServiceImpl.getInstance()

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            product = self.productService.createProduct(serializer.validated_data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
