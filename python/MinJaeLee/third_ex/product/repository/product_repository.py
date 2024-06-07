from abc import ABC, abstractmethod


class productRepository(ABC):
    @abstractmethod
    def getProductList(self):
        pass