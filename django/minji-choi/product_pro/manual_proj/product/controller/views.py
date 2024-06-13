from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from product.entity.models import Product
from product.serializers import ProductSerializer
from product.service.product_service_impl import ProductServiceImpl

class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all()
    productService = ProductServiceImpl.getInstance()

    def list(self, request):
        productList = self.productService.list()
        serializer = ProductSerializer(productList, many=True)
        return Response(serializer.data)

    def register (self, request):
        try:
            data = request.data

            productImage = request.FILES.get('productImage')
            prodname = data.get('prodname')
            writer = data.get('writer')
            price = data.get('price')
            content = data.get('content')
            if not all ([productImage, prodname, writer,price, content]):
                return Response({'error': '모든 내용을 채워주세요!'}, status=status.HTTP_400_BAD_REQUEST)

            self.productService.createProduct(prodname, price, writer, content, productImage)
            serializer = ProductSerializer(data=request.data)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('상품 등록 과정 중 문제 발생: ', e)
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)

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
