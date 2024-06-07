from abc import ABC, abstractmethod

class ProductService(ABC):

    @abstractmethod
    def displayProductList(self):
        pass

    @abstractmethod
    def getProductList(self):
        pass