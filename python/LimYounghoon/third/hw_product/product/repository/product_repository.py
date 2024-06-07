from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    def create(self, productList):
        pass

    @abstractmethod
    def getProductList(self):
        pass

    @abstractmethod
    def list(self):
        pass
