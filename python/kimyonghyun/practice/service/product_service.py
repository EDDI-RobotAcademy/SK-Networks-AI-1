from abc import ABC, abstractmethod


class ProductService(ABC):
    @abstractmethod
    def create(self, productname):
        pass

    @abstractmethod
    def findProductByProductname(self, productname):
        pass

    @abstractmethod
    def getProductList(self):
        pass
