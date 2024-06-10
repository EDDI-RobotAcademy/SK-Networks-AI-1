from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    def create(self, productData):
        pass