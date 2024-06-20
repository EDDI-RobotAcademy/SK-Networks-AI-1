from abc import ABC, abstractmethod

class ProductRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, productName, productPrice, productDescription, productImage):
        pass

    @abstractmethod
    def findByProductId(self):
        pass

