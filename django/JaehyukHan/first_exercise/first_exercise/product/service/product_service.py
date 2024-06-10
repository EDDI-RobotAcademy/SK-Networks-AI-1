from abc import ABC, abstractmethod

class ProductService(ABC):
    @abstractmethod
    def createProduct(self, productData):
        pass