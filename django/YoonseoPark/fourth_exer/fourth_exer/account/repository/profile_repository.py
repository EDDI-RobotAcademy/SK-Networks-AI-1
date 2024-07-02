from abc import ABC, abstractmethod


class ProfileRepository(ABC):

    @abstractmethod
    def findByEmail(self, email):
        pass

    @abstractmethod
    def findByNickname(self, nickname):
        pass

    @abstractmethod
    def create(self, nickname, email, account):
        pass