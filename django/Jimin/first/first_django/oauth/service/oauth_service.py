from abc import abstractmethod, ABC

class OauthService(ABC):

    @abstractmethod
    def kakaoLoginAddress(self):
        pass

    @abstractmethod
    def requestAccessToken(self, kakaoAuthCode):
        pass