from abc import abstractmethod, ABC


class CartRepository(ABC):

    @abstractmethod
    def findByAccount(self, account):
        pass

    @abstractmethod
    def register(self, account):
        pass

