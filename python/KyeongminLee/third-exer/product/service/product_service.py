from abc import ABC, abstractmethod


class ProductService(ABC):
    @abstractmethod
    def createProduct(self, producntName):
        pass

    @abstractmethod
    def getProductList(self):
        pass