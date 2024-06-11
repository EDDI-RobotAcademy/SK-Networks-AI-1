from abc import ABC, abstractmethod

class ProductService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def resisterProduct(self, productInfo):
        pass

    @abstractmethod
    def readProduct(self, productID):
        pass

    @abstractmethod
    def removeProoduct(self, productID):
        pass

    @abstractmethod
    def updateProduct(self, productID, productInfo):
        pass
