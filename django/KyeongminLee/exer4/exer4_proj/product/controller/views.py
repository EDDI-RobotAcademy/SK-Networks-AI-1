from django.shortcuts import render
from rest_framework import viewsets
from product.entity.models import Product
from product.serializers import ProductSerializer
from product.service.prodcut_service_impl import ProductServiceImpl


# Create your views here.
class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all()
    productService = ProductServiceImpl.getInstance()

