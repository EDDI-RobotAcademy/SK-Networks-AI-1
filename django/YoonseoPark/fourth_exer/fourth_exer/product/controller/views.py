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
        print('productList:', productList)
        serializer = ProductSerializer(productList, many=True)
        print('serialized productList:', serializer.data)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            product = self.productService.createProduct(serializer.validated_data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        product = self.productService.readProductInfo(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
