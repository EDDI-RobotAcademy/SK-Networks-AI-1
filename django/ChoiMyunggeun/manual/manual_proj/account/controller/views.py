from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.serializers import AccountSerializer
from account.service.account_service_impl import AccountServiceImpl


class AccountView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()

    def checkEmailDuplication(self, request):
        # url = self.oauthService.kakaoLoginAddress()
        print("checkEmailDuplication()")

        try:
            email = request.data.get('email')
            isDuplicate = self.accountService.checkEmailDuplication(email)

            return Response({'isDuplicate': isDuplicate, 'message': 'Email이 이미 존재' \
                             if isDuplicate else 'Email 사용 가능'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("이메일 중복 체크 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def checkNicknameDuplication(self, request):
        print("checkNicknameDuplication()")

        try:
            nickname = request.data.get('newNickname')
            print(f"nickname: {nickname}")
            isDuplicate = self.accountService.checkNicknameDuplication(nickname)

            return Response({'isDuplicate': isDuplicate, 'message': 'Nickname이 이미 존재' \
                             if isDuplicate else 'Nickname 사용 가능'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("닉네임 중복 체크 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def registerAccount(self, request):
        try:
            nickname = request.data.get('nickname')
            email = request.data.get('email')

            account = self.accountService.registerAccount(
                loginType='KAKAO',
                roleType='NORMAL',
                nickname=nickname,
                email=email,
            )

            serializer = AccountSerializer(account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("계정 생성 중 에러 발생:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)