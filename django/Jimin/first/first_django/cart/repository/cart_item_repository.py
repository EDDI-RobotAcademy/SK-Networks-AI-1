from abc import ABC, abstractmethod

class CartItemRepository(ABC):
    @abstractmethod
    def register(self, cartData, cart, product):
        pass

    @abstractmethod
    def update(self, cartItem):
        pass

    @abstractmethod
    def findByProductId(self, productId):
        pass