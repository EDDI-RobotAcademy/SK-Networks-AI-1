from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from cart.entity.cart import Cart
from cart.service.cart_service_impl import CartServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl
from account.service.account_service_impl import AccountServiceImpl
import uuid

# Create your views here.


class CartView(viewsets.ViewSet):
    cartService = CartServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def cartRegister(self, request):
        try:
            data= request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            self.cartService.cartRegister(data, accountId)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('상픔 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


