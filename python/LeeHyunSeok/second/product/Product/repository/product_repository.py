from abc import ABC,abstractmethod

class ProductRepository(ABC):


    @abstractmethod
    def getProductList(self):
        pass