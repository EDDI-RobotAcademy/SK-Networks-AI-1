from rest_framework import viewsets, status
from rest_framework.response import Response

from account.entity.account import Account
from account.service.account_service_impl import AccountServiceImpl


class AccountView(viewsets.ViewSet):
    queryset = Account.objects.all()
    accountService = AccountServiceImpl.getInstance()

    def checkEmailDuplication(self, request):
        print("checkEmailDuplication()")

        try:
            email = request.data.get('email')
            isDuplicate = self.accountService.checkEmailDuplication(email)
            
            return Response({'isDuplicate': isDuplicate, 'message': 'Email이 이미 존재'
                             if isDuplicate else 'Email 사용 가능'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("이메일 중복 체크 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)