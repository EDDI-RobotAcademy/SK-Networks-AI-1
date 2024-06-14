from django.shortcuts import render
from rest_framework import viewsets


class AccountView(viewsets.ViewSet):
    # oauthService = OauthServiceImpl.getInstance()

    # 사용자가 '카카오 로그인' 버튼을 눌러 요청시 로그인 경로를 리턴
    def checkEmailDuplication(self, request):
        # url = self.oauthService.kakaoLoginAddress()
        print("checkEmailDuplication()")


