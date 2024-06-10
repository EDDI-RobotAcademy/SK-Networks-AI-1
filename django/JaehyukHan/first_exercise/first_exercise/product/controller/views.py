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

