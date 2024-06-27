from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from cart.controller.response_form.cart_item_response_form import CartItemResponseForm
from cart.entity.cart import Cart
from cart.service.cart_service_impl import CartServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl


# Create your views here.
class CartView(viewsets.ViewSet):
    cartService = CartServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    queryset = Cart.objects.all()

    def cartRegister(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            self.cartService.cartRegister(data, accountId)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            return Response({ 'error': str(e) }, status=status.HTTP_400_BAD_REQUEST)

    def cartItemList(self, request):
        # 내가 작성한 코드
        # userToken = request.data.get('userToken')
        # accountId = self.redisService.getValueByKey(userToken)
        # cartList = self.cartService.cartList(accountId)
        #
        # return Response(CartItemResponseForm(
        #     cartList=cartList
        # ))
        data = request.data
        userToken = data.get('userToken')

        if not userToken:
            return Response({ 'error': 'User token is required' }, status=status.HTTP_400_BAD_REQUEST)

        accountId = self.redisService.getValueByKey(userToken)
        if not accountId:
            return Response({ 'error': 'Invalid user token' }, status=status.HTTP_400_BAD_REQUEST)

        cartItemListResponseForm = self.cartService.cartList(accountId)
        return Response(cartItemListResponseForm, status=status.HTTP_200_OK)
