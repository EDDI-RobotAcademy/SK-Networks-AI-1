from manual_proj import settings
from oauth.service.oauth_service import OauthService

import requests


class OauthServiceImpl(OauthService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.loginUrl = settings.KAKAO['LOGIN_URL']
            cls.__instance.clientId = settings.KAKAO['CLIENT_ID']
            cls.__instance.redirectUri = settings.KAKAO['REDIRECT_URI']
            cls.__instance.tokenRequestUri = settings.KAKAO['TOKEN_REQUEST_URI']
            cls.__instance.userinfoRequestUri = settings.KAKAO['USERINFO_REQUEST_URI']

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#request-code
    def kakaoLoginAddress(self):
        print("kakaoLoginAddress()")
        return (f"{self.loginUrl}/oauth/authorize?"
                f"client_id={self.clientId}&redirect_uri={self.redirectUri}&response_type=code")

    def requestAccessToken(self, kakaoAuthCode):
        print("requestAccessToken()")
        accessTokenRequestForm = {
            'grant_type': 'authorization_code',
            'client_id': self.clientId,
            'redirect_uri': self.redirectUri,
            'code': kakaoAuthCode,
            'client_secret': None
        }

        print(f"client_id: {self.clientId}")
        print(f"redirect_uri: {self.redirectUri}")
        print(f"code: {kakaoAuthCode}")
        print(f"tokenRequestUri: {self.tokenRequestUri}")

        response = requests.post(self.tokenRequestUri, data=accessTokenRequestForm)
        print(f"response: {response}")

        return response.json()

    def requestUserInfo(self, accessToken):
        headers = {'Authorization': f'Bearer {accessToken}'}
        response = requests.post(self.userinfoRequestUri, headers=headers)
        return response.json()


