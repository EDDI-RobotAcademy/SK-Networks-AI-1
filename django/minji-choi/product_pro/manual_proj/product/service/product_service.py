from abc import ABC, abstractmethod


class ProductService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createProduct(self,productName, productPrice, writer, productCategory, content, productImage):
        pass
    @abstractmethod
    def readProduct(self, productId):
        pass
    @abstractmethod
    def removeProduct(self, productId):
        pass

    @abstractmethod
    def updateProduct(self, productId, productData):
        pass
