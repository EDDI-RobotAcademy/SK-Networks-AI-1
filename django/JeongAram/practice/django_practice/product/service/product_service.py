from abc import ABC, abstractmethod

class ProductService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def registerProduct(self, productInfo):
        pass

    @abstractmethod
    def readProduct(self, productID):
        pass

    @abstractmethod
    def removeProduct(self, productID):
        pass

    @abstractmethod
    def updateProduct(self, productID, productInfo):
        pass
