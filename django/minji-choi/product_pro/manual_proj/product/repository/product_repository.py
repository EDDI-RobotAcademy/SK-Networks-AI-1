from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, productName, productPrice, writer, productCategory, content, productImage):
        pass

    @abstractmethod
    def findByProductId(self, productId):
        pass

    @abstractmethod
    def deleteByProductId(self, productId):
        pass
    @abstractmethod
    def update(self, product, productData):
        pass
