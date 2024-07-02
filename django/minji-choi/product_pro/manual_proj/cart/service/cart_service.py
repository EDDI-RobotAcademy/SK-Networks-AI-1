from abc import ABC, abstractmethod

class CartService(ABC):
    @abstractmethod
    def cartList(self, accountId):
        pass
    @abstractmethod
    def cartRegister(self, cartData, account):
        pass

    @abstractmethod
    def removeCartItem(self, accountId, cartItemId):
        pass
