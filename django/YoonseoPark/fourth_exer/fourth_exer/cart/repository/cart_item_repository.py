from abc import ABC, abstractmethod

class CartItemRepository(ABC):

    @abstractmethod
    def findByProductName(self, productName):
        pass

    @abstractmethod
    def register(self, cartData, cart, product):
        pass