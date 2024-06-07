from abc import ABC, abstractmethod


class ProductService(ABC):
    @abstractmethod
    def createProduct(self, prod):
        pass

    @abstractmethod
    def getProductList(self):
        pass