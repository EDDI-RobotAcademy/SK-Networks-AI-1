from abc import ABC, abstractmethod


class AccountRepository(ABC):
    @abstractmethod
    def create(self, loginType, roleType):
        pass

    def findById(self, accountId):
        pass