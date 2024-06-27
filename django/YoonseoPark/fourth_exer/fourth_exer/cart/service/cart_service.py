from abc import ABC, abstractmethod


class CartService(ABC):
    @abstractmethod
    def registerCart(self, cartData, accountId):
        pass

    @abstractmethod
    def cartList(self, accountId):
        pass