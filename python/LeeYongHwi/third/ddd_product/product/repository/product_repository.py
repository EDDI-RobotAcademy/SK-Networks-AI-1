from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    def create(self, prod):
        pass
    @abstractmethod
    def getProductList(self):
        pass