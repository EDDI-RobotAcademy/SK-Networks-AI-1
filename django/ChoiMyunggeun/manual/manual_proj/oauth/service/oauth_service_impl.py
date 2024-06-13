from oauth.service.oauth_service import OauthService


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

        return cls.__instance

    # https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#request-code
    def kakaoLoginAddress(self):
        print("kakaoLoginAddress()")
        return (f"{self.loginUrl}/oauth/authorize?"
                f"client_id={self.clientId}&redirect_uri={self.redirectUri}&response_type=code")
