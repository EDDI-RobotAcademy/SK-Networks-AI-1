from abc import ABC, abstractmethod


class CartRepository(ABC):
    @abstractmethod
    def register(self, cartData):
        pass
