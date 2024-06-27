from abc import ABC, abstractmethod

from cart.entity.cart_item import CartItem


class CartItemRepository(ABC):
    @abstractmethod
    def register(self, cartData, cart, product):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findByCart(self, cart):
        pass

    @abstractmethod
    def findByProductId(self, productId):
        pass

    @abstractmethod
    def findAllByProductId(self, productId):
        pass

    @abstractmethod
    def update(self, cartItem):
        pass