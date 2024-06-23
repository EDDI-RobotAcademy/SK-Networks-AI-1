from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    def create(self, productData):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def findByProductId(self, productId):
        pass