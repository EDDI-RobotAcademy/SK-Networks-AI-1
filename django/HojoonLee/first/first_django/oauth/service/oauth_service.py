from abc import ABC, abstractmethod


class OauthService(ABC):

    @abstractmethod
    def kakaoLoginAddress(self):
        pass