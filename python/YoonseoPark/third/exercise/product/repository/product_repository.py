from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    def createProductList(self, productName):
        pass

    @abstractmethod
    def getProductList(self):
        pass