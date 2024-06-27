from abc import abstractmethod, ABC


class ProductService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createProduct(self, productName, productPrice, productDescription, productImage):
        pass

    @abstractmethod
    def readProduct(self, productId):
        pass
