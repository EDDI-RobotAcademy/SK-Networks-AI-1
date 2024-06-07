from abc import ABC,abstractmethod

class ProductService(ABC):


    @abstractmethod
    def getProductList(self):
        pass
    @abstractmethod
    def displayProductList(self):
        pass