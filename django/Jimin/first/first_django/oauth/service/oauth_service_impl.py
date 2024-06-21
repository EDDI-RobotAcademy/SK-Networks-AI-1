from first_django import settings
from oauth.service.oauth_service import OauthService

import requests


class OauthServiceImpl(OauthService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

            cls.__instance.loginUrl = settings.KAKAO['LOGIN_URL']
            cls.__instance.clientId = settings.KAKAO['CLIENT_ID']
            cls.__instance.redirectUri = settings.KAKAO['REDIRECT_URI']
            cls.__instance.tokenRequestUri = settings.KAKAO['TOKEN_REQUEST_URI']
            cls.__instance.userinfoRequestUri = settings.KAKAO['USERINFO_REQUEST_URI']

        return cls.__instance

    def kakaoLoginAddress(self):
        print("kakaoLoginAddress")
        return f"{self.loginUrl}/oauth/authorize?client_id={self.clientId}&redirect_uri={self.redirectUri}&response_type=code"

    def requestAccessToken(self, kakaoAuthCode):
        print("requestAccessToken()")
        accessTokenRequestForm = {
            'grant_type': 'authorization_code',
            'client_id': self.clientId,
            'redirect_uri': self.redirectUri,
            'code': kakaoAuthCode,
            'client_secret': None
        }

        response = requests.post(self.tokenRequestUri, data=accessTokenRequestForm)
        return response.json()

    def requestUserInfo(self, accessToken):
        headers = {'Authorization': f'Bearer {accessToken}'}
        response = requests.post(self.userinfoRequestUri, headers=headers)
        return response.json()


