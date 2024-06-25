from abc import ABC, abstractmethod


class CartService(ABC):
    @abstractmethod
    def cartRegister(self, cartData, accountId):
        pass

    @abstractmethod
    def cartList(self, accountId):
        pass
