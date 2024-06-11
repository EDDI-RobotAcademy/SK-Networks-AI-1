from abc import ABC, abstractmethod

class ProductRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def resister(self, productData):
        pass