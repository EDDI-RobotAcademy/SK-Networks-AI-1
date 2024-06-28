from abc import ABC, abstractmethod


class CartItemRepository(ABC):
    @abstractmethod
    def register(self, cartData, cart, product):
        pass

    @abstractmethod
    def findByProduct(self, product):
        pass

    @abstractmethod
    def findAllByProductId(self, productId):
        pass

    @abstractmethod
    def update(self, cartItem):
        pass

    @abstractmethod
    def findByCart(self, cart):
        pass

    @abstractmethod
    def findById(self, id):
        pass