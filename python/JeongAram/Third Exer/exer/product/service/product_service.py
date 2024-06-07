from abc import ABC, abstractmethod


class ProductService(ABC):
    @abstractmethod
    def createProductList(self, productName):
        pass

    @abstractmethod
    def getProductList(self):
        pass