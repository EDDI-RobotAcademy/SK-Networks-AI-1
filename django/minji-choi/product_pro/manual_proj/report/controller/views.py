from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from report.service.report_service_impl import ReportServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl


class ReportView(viewsets.ViewSet):
    reportService = ReportServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def reportCreate(self, request):
        try:
            print('data: ', request.data)
            userToken = request.data.get('userToken')
            data = request.data.get('data')
            age = data.get('age')
            gender = data.get('gender')
            # print('유저 토큰 : ', userToken)
            # print('age : ', age)
            # print('gender: ', gender)
            accountId = self.redisService.getValueByKey(userToken)
            print('accountId: ', accountId)
            self.reportService.createReport(age, gender, accountId)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('사용자 리포트 생성 중 에러 발생: ', e)
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)