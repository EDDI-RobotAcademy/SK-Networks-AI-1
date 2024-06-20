from abc import abstractmethod, ABC


class ProductService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createProduct(self, productName, productPrice, productDescription, productImage):
        pass

    @abstractmethod
    def createProduct(self, productName, productPrice, productDesctiption, productImage):
        return self.__productRepository.create(
            productName, productPrice, productDesctiption, productImage
        )

    def readProduct(self, productId):
        return self.__productRepository.findByProductId(productId)
