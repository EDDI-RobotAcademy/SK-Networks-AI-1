from abc import ABC, abstractmethod

class ProductService(ABC):

    @abstractmethod
    def productList(self):
        pass