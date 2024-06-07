from abc import ABC, abstractmethod


class ProductService(ABC):
    @abstractmethod
    def createProduct(self, productList):
        pass

    @abstractmethod
    def getProductList(self):
        pass
