from abc import abstractmethod, ABC


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

    @abstractmethod
    def findAllByProductId(self, productId):
        pass

    @abstractmethod
    def findByCart(self, cart):
        pass

    @abstractmethod
    def findById(self, id):
        pass