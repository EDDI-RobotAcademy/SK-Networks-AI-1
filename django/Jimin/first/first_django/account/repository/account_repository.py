from abc import abstractmethod, ABC

class AccountRepository(ABC):
    @abstractmethod
    def create(self, loginType, roleType):
        pass