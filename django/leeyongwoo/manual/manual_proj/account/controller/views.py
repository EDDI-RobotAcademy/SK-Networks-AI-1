from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl

class AccountView(viewsets.ViewSet):

    accountService = AccountServiceImpl.getInstance()

    def checkEmailDuplication(self,request):
        print('checkEmailDuplication')

        try:
            email = request.data.get('email')
            isDuplicate = self.accountService.checkEmailDuplication(email)

            return Response({'isDuplicate': isDuplicate, 'message': 'email이 이미 있습니다.'\
                             if isDuplicate else 'email이 사용 가능합니다.'},status=status.HTTP_200_OK)
        except Exception as e:
            print('이메일 중복체크 중 오류 발생:',e)
            return Response({'error': str(e)},status=status.HTTP_400_BAD_REQUEST)
