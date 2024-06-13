from abc import abstractmethod, ABC


class OauthService(ABC):
    @abstractmethod
    def kakaoLoginAddress(self):
        pass

