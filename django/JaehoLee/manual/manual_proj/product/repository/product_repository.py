from abc import abstractmethod, ABC


class ProductRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, productName, productPrice, productDescription, productImage):
        pass

    @abstractmethod
    def findByProductId(self, productId):
        pass
