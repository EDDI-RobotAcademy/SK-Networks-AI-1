from rest_framework import viewsets, status
from rest_framework.response import Response
from oauth.service.redis_service_impl import RedisServiceImpl
from orders.service.order_service_impl import OrderServiceImpl
class OrdersView(viewsets.ViewSet):
    orderService = OrderServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    # 장바구니에서 confirm한 요청이 들어온다.
    def createOrders(self, request):
        try:
            data = request.data
            print('data :', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            if not accountId:
                raise ValueError('Invalid User Token')

            orderItemList = data.get('items')
            print(f"orderItemList : {orderItemList}")

            # 고객 id와 고객이 산 물품들을 가지고 주문 번호를 만든다.
            orderId = self.orderService.createOrder(accountId, orderItemList)
            print(f"orderId : {orderId}")
            return Response(orderId, status=status.HTTP_200_OK) # 돈이 쓰이는 과정이라 유저 정보 항상 확인

        except Exception as e:
            print('주문 과정 중 에러 발생')
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
