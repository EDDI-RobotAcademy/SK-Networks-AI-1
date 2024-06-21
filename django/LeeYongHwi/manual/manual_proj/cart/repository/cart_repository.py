from abc import abstractmethod, ABC


class CartRepository(ABC):
    @abstractmethod
    def register(self, account):
        pass

    @abstractmethod
    def findByAccount(self, account):
        pass

